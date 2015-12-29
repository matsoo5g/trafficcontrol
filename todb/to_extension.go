// Copyright 2015 Comcast Cable Communications Management, LLC

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

// http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// This file was initially generated by gen_goto2.go (add link), as a start
// of the Traffic Ops golang data model

package todb

import (
	"encoding/json"
	"fmt"
	"gopkg.in/guregu/null.v3"
	"time"
)

type ToExtension struct {
	Id                    int64       `db:"id" json:"id"`
	Name                  string      `db:"name" json:"name"`
	Version               string      `db:"version" json:"version"`
	InfoUrl               string      `db:"info_url" json:"infoUrl"`
	ScriptFile            string      `db:"script_file" json:"scriptFile"`
	Isactive              int64       `db:"isactive" json:"isactive"`
	AdditionalConfigJson  null.String `db:"additional_config_json" json:"additionalConfigJson"`
	Description           null.String `db:"description" json:"description"`
	ServercheckShortName  null.String `db:"servercheck_short_name" json:"servercheckShortName"`
	ServercheckColumnName null.String `db:"servercheck_column_name" json:"servercheckColumnName"`
	Type                  int64       `db:"type" json:"type"`
	LastUpdated           time.Time   `db:"last_updated" json:"lastUpdated"`
}

func handleToExtension(method string, id int, payload []byte) (interface{}, error) {
	if method == "GET" {
		return getToExtension(id)
	} else if method == "POST" {
		return postToExtension(payload)
	} else if method == "PUT" {
		return putToExtension(id, payload)
	} else if method == "DELETE" {
		return delToExtension(id)
	}
	return nil, nil
}

func getToExtension(id int) (interface{}, error) {
	ret := []ToExtension{}
	if id >= 0 {
		err := globalDB.Select(&ret, "select * from to_extension where id=$1", id)
		if err != nil {
			fmt.Println(err)
			return nil, err
		}
	} else {
		queryStr := "select * from to_extension"
		err := globalDB.Select(&ret, queryStr)
		if err != nil {
			fmt.Println(err)
			return nil, err
		}
	}
	return ret, nil
}

func postToExtension(payload []byte) (interface{}, error) {
	var v Asn
	err := json.Unmarshal(payload, &v)
	if err != nil {
		fmt.Println(err)
	}
	sqlString := "INSERT INTO to_extension("
	sqlString += "name"
	sqlString += ",version"
	sqlString += ",info_url"
	sqlString += ",script_file"
	sqlString += ",isactive"
	sqlString += ",additional_config_json"
	sqlString += ",description"
	sqlString += ",servercheck_short_name"
	sqlString += ",servercheck_column_name"
	sqlString += ",type"
	sqlString += ") VALUES ("
	sqlString += ":name"
	sqlString += ",:version"
	sqlString += ",:info_url"
	sqlString += ",:script_file"
	sqlString += ",:isactive"
	sqlString += ",:additional_config_json"
	sqlString += ",:description"
	sqlString += ",:servercheck_short_name"
	sqlString += ",:servercheck_column_name"
	sqlString += ",:type"
	sqlString += ")"
	result, err := globalDB.NamedExec(sqlString, v)
	if err != nil {
		fmt.Println(err)
		return nil, err
	}
	return result, err
}

func putToExtension(id int, payload []byte) (interface{}, error) {
	// Note this depends on the json having the correct id!
	var v Asn
	err := json.Unmarshal(payload, &v)
	if err != nil {
		fmt.Println(err)
		return nil, err
	}
	v.LastUpdated = time.Now()
	sqlString := "UPDATE to_extension SET "
	sqlString += "name = :name"
	sqlString += ",version = :version"
	sqlString += ",info_url = :info_url"
	sqlString += ",script_file = :script_file"
	sqlString += ",isactive = :isactive"
	sqlString += ",additional_config_json = :additional_config_json"
	sqlString += ",description = :description"
	sqlString += ",servercheck_short_name = :servercheck_short_name"
	sqlString += ",servercheck_column_name = :servercheck_column_name"
	sqlString += ",type = :type"
	sqlString += ",last_updated = :last_updated"
	sqlString += " WHERE id=:id"
	result, err := globalDB.NamedExec(sqlString, v)
	if err != nil {
		fmt.Println(err)
		return nil, err
	}
	return result, err
}

func delToExtension(id int) (interface{}, error) {
	result, err := globalDB.NamedExec("DELETE FROM to_extension WHERE id=:id", id)
	if err != nil {
		fmt.Println(err)
		return nil, err
	}
	return result, err
}
