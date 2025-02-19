#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# RPM spec file for Traffic Stats (tm).
#
%define debug_package %{nil}
Name:     trafficcontrol-cache-config
Summary:  Installs Traffic Control cache configuration tools
Version:  %{traffic_control_version}
Release:  %{build_number}
License:  Apache License, Version 2.0
Group:    Applications/Communications
Source0:  trafficcontrol-cache-config-%{version}.tgz
URL:      https://github.com/apache/trafficcontrol/
Vendor:   Apache Software Foundation
Packager: dev at trafficcontrol dot Apache dot org
%{?el6:Requires: git, perl}
%{?el7:Requires: git, perl}
%{?el8:Requires: git, perl}


%description
Installs Traffic Control Cache Configuration utilities. See the `t3c` application.

%prep
tar xvf %{SOURCE0} -C $RPM_SOURCE_DIR


%build
set -o nounset
# copy license
cp "${TC_DIR}/LICENSE" %{_builddir}

ccdir="cache-config"
ccpath="src/github.com/apache/trafficcontrol/${ccdir}/"

# copy t3c binary
got3cdir="$ccpath"/t3c
( mkdir -p "$got3cdir" && \
	cd "$got3cdir" && \
	cp "$TC_DIR"/"$ccdir"/t3c/t3c .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }

# copy t3c-apply binary
go_t3c_apply_dir="$ccpath"/t3c-apply
( mkdir -p "$go_t3c_apply_dir" && \
	cd "$go_t3c_apply_dir" && \
	cp "$TC_DIR"/"$ccdir"/t3c-apply/t3c-apply .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }

# copy t3c-generate binary
godir="$ccpath"/t3c-generate
( mkdir -p "$godir" && \
	cd "$godir" && \
	cp "$TC_DIR"/"$ccdir"/t3c-generate/t3c-generate .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }

# copy t3c-request binary
go_toreq_dir="$ccpath"/t3c-request
( mkdir -p "$go_toreq_dir" && \
	cd "$go_toreq_dir" && \
	cp "$TC_DIR"/"$ccdir"/t3c-request/t3c-request .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }

# copy t3c-update binary
go_toupd_dir="$ccpath"/t3c-update
( mkdir -p "$go_toupd_dir" && \
	cd "$go_toupd_dir" && \
	cp "$TC_DIR"/"$ccdir"/t3c-update/t3c-update .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }

# copy t3c-check binary
go_t3c_check_dir="$ccpath"/t3c-check
( mkdir -p "$go_t3c_check_dir" && \
	cd "$go_t3c_check_dir" && \
	cp "$TC_DIR"/"$ccdir"/t3c-check/t3c-check .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }

# copy t3c-check-refs binary
go_t3c_check_refs_dir="$ccpath"/t3c-check-refs
( mkdir -p "$go_t3c_check_refs_dir" && \
	cd "$go_t3c_check_refs_dir" && \
	cp "$TC_DIR"/"$ccdir"/t3c-check-refs/t3c-check-refs .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }

# copy t3c-diff binary
go_t3c_diff_dir="$ccpath"/t3c-diff
( mkdir -p "$go_t3c_diff_dir" && \
	cd "$go_t3c_diff_dir" && \
	cp "$TC_DIR"/"$ccdir"/t3c-diff/t3c-diff .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }

# copy t3c-diff binary
go_t3c_check_reload_dir="$ccpath"/t3c-check-reload
( mkdir -p "$go_t3c_check_reload_dir" && \
	cd "$go_t3c_check_reload_dir" && \
	cp "$TC_DIR"/"$ccdir"/t3c-check-reload/t3c-check-reload .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }

# copy t3c-preprocess binary
go_t3c_preprocess_dir="$ccpath"/t3c-preprocess
( mkdir -p "$go_t3c_preprocess_dir" && \
	cd "$go_t3c_preprocess_dir" && \
	cp "$TC_DIR"/"$ccdir"/t3c-preprocess/t3c-preprocess .
) || { echo "Could not copy go program at $(pwd): $!"; exit 1; }



%install
ccdir="cache-config/"
installdir="/usr/bin"

mkdir -p ${RPM_BUILD_ROOT}/"$installdir"
mkdir -p "${RPM_BUILD_ROOT}"/etc/logrotate.d
mkdir -p "${RPM_BUILD_ROOT}"/var/log/trafficcontrol-cache-config

cp -p ${RPM_SOURCE_DIR}/trafficcontrol-cache-config-%{version}/traffic_ops_ort.pl ${RPM_BUILD_ROOT}/"$installdir"
cp -p ${RPM_SOURCE_DIR}/trafficcontrol-cache-config-%{version}/supermicro_udev_mapper.pl ${RPM_BUILD_ROOT}/"$installdir"

src=src/github.com/apache/trafficcontrol/cache-config
cp -p ${RPM_SOURCE_DIR}/trafficcontrol-cache-config-%{version}/build/atstccfg.logrotate "${RPM_BUILD_ROOT}"/etc/logrotate.d/atstccfg
touch ${RPM_BUILD_ROOT}/var/log/trafficcontrol-cache-config/atstccfg.log

cp -p "$src"/t3c-generate/t3c-generate ${RPM_BUILD_ROOT}/"$installdir"

t3csrc=src/github.com/apache/trafficcontrol/"$ccdir"/t3c
cp -p "$t3csrc"/t3c ${RPM_BUILD_ROOT}/"$installdir"

t3c_apply_src=src/github.com/apache/trafficcontrol/"$ccdir"/t3c-apply
cp -p "$t3c_apply_src"/t3c-apply ${RPM_BUILD_ROOT}/"$installdir"

to_req_src=src/github.com/apache/trafficcontrol/"$ccdir"/t3c-request
cp -p "$to_req_src"/t3c-request ${RPM_BUILD_ROOT}/"$installdir"

to_upd_src=src/github.com/apache/trafficcontrol/"$ccdir"/t3c-update
cp -p "$to_upd_src"/t3c-update ${RPM_BUILD_ROOT}/"$installdir"

t3c_diff_src=src/github.com/apache/trafficcontrol/"$ccdir"/t3c-diff
cp -p "$t3c_diff_src"/t3c-diff ${RPM_BUILD_ROOT}/"$installdir"

t3c_check_src=src/github.com/apache/trafficcontrol/"$ccdir"/t3c-check
cp -p "$t3c_check_src"/t3c-check ${RPM_BUILD_ROOT}/"$installdir"

t3c_check_refs_src=src/github.com/apache/trafficcontrol/"$ccdir"/t3c-check-refs
cp -p "$t3c_check_refs_src"/t3c-check-refs ${RPM_BUILD_ROOT}/"$installdir"

t3c_check_reload_src=src/github.com/apache/trafficcontrol/"$ccdir"/t3c-check-reload
cp -p "$t3c_check_reload_src"/t3c-check-reload ${RPM_BUILD_ROOT}/"$installdir"

t3c_preprocess_src=src/github.com/apache/trafficcontrol/"$ccdir"/t3c-preprocess
cp -p "$t3c_preprocess_src"/t3c-preprocess ${RPM_BUILD_ROOT}/"$installdir"

%clean
rm -rf ${RPM_BUILD_ROOT}

%post

%files
%license LICENSE
%attr(755, root, root)
/usr/bin/traffic_ops_ort.pl
/usr/bin/supermicro_udev_mapper.pl
/usr/bin/t3c
/usr/bin/t3c-apply
/usr/bin/t3c-check
/usr/bin/t3c-check-refs
/usr/bin/t3c-check-reload
/usr/bin/t3c-diff
/usr/bin/t3c-generate
/usr/bin/t3c-preprocess
/usr/bin/t3c-request
/usr/bin/t3c-update

%config(noreplace) /etc/logrotate.d/atstccfg
%config(noreplace) /var/log/trafficcontrol-cache-config/atstccfg.log

%changelog
