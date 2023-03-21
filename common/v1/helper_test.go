//
// DISCLAIMER
//
// Copyright 2023 ArangoDB GmbH, Cologne, Germany
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Copyright holder is ArangoDB GmbH, Cologne, Germany
//

package v1

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGetValue(t *testing.T) {
	list := []*KeyValuePair{
		{
			Key:   "foo",
			Value: "bar",
		},
		{
			Key:   "empty",
			Value: "",
		},
		{
			Key:   "bar",
			Value: "isclosed",
		},
	}

	assert.Nil(t, KeyValuePairList(list).GetValue("non-exist"))
	assert.Equal(t, "bar", toString(KeyValuePairList(list).GetValue("foo")))
	assert.NotNil(t, KeyValuePairList(list).GetValue("empty"))
	assert.Equal(t, "", toString(KeyValuePairList(list).GetValue("empty")))
	assert.Equal(t, "isclosed", toString(KeyValuePairList(list).GetValue("bar")))
}

func TestUpsertPair(t *testing.T) {
	list := KeyValuePairList{
		{
			Key:   "foo",
			Value: "bar",
		},
		{
			Key:   "empty",
			Value: "",
		},
		{
			Key:   "bar",
			Value: "isclosed",
		},
	}

	assert.False(t, list.UpsertPair("foo", "new-bar"))
	assert.Equal(t, "new-bar", toString(list.GetValue("foo")))
	assert.Len(t, list, 3)

	assert.True(t, list.UpsertPair("new", "new-new"))
	assert.Equal(t, "new-new", toString(list.GetValue("new")))
	assert.Len(t, list, 4)
}

func TestRemovePairByKeyTest(t *testing.T) {
	list := KeyValuePairList{
		{
			Key:   "foo",
			Value: "bar",
		},
		{
			Key:   "empty",
			Value: "",
		},
		{
			Key:   "bar",
			Value: "isclosed",
		},
	}
	validationList1 := KeyValuePairList{
		{
			Key:   "foo",
			Value: "bar",
		},
		{
			Key:   "empty",
			Value: "",
		},
		{
			Key:   "bar",
			Value: "isclosed",
		},
	}
	validationList2 := KeyValuePairList{
		{
			Key:   "empty",
			Value: "",
		},
		{
			Key:   "bar",
			Value: "isclosed",
		},
	}

	assert.False(t, list.RemovePairByKey("non-existent"))
	assert.Len(t, list, 3)
	assert.EqualValues(t, validationList1, list)

	assert.True(t, list.RemovePairByKey("foo"))
	assert.Len(t, list, 2)
	assert.EqualValues(t, validationList2, list)
}

// toString makes from a *string a string
// Note we do not want to include refs-helper inside integration-apis, because that results in a circular reference
func toString(v *string) string {
	if v == nil {
		return ""
	}
	return *v
}
