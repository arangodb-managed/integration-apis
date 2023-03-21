//
// DISCLAIMER
//
// Copyright 2020 ArangoDB GmbH, Cologne, Germany
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
// Author Ewout Prangsma
//

package v1

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGroupURL(t *testing.T) {
	assert.Equal(t, "/Organization/123/Group/c1", GroupURL("123", "c1"))
	assert.Equal(t, "/Organization/123%2F567/Group/c2%2F3", GroupURL("123/567", "c2/3"))
	assert.Equal(t, "/Organization/123%2F567/Group/e%25f", GroupURL("123/567", "e%f"))
}

func TestRoleURL(t *testing.T) {
	assert.Equal(t, "/Organization/123/Role/c1", RoleURL("123", "c1"))
	assert.Equal(t, "/Organization/123%2F567/Role/c2%2F3", RoleURL("123/567", "c2/3"))
	assert.Equal(t, "/Organization/123%2F567/Role/e%25f", RoleURL("123/567", "e%f"))
}

func TestUserURL(t *testing.T) {
	assert.Equal(t, "/User/c1", UserURL("c1"))
	assert.Equal(t, "/User/123%2F567", UserURL("123/567"))
	assert.Equal(t, "/User/e%25f", UserURL("e%f"))
}

func TestAPIKeyURL(t *testing.T) {
	assert.Equal(t, "/User/123/APIKey/c1", APIKeyURL("123", "c1"))
	assert.Equal(t, "/User/123%2F567/APIKey/c2%2F3", APIKeyURL("123/567", "c2/3"))
	assert.Equal(t, "/User/123%2F567/APIKey/e%25f", APIKeyURL("123/567", "e%f"))
}
