#!/usr/bin/env bash
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

trap 'echo "Error on line ${LINENO} of ${0}"; exit 1' ERR;
set -o errexit -o nounset;

source /to-access.sh;

# Source the CIAB-CA shared SSL environment
until [[ -v 'X509_GENERATION_COMPLETE' ]]; do
  echo 'Waiting on X509 vars to be defined';
  sleep 1;
  if [[ ! -e "$X509_CA_ENV_FILE" ]]; then
    continue;
  fi;
  source "$X509_CA_ENV_FILE";
done;

cat "$X509_CA_CERT_FULL_CHAIN_FILE" >> /etc/ssl/cert.pem;

# It crashes if STARTTLS is not hidden, see maildev/maildev#274
exec bin/maildev \
  --smtp="$SMTP_PORT" \
  --hide-extensions='STARTTLS' \
  --https \
  --web=443 \
  --https-key="${X509_CA_DIR}/${INFRA_SUBDOMAIN}.${TLD_DOMAIN}.key" \
  --https-cert="${X509_CA_DIR}/${INFRA_SUBDOMAIN}.${TLD_DOMAIN}.crt";
