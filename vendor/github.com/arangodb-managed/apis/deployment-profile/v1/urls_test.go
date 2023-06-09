//
// DISCLAIMER
//
// Copyright 2022 ArangoDB GmbH, Cologne, Germany
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
//

package v1

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDeploymentProfileURL(t *testing.T) {
	assert.Equal(t, "/Organization/123/DeploymentProfile/12345", DeploymentProfileURL("123", "12345"))
	assert.Equal(t, "/Organization/123%2F654/DeploymentProfile/123%2F456", DeploymentProfileURL("123/654", "123/456"))
	assert.Equal(t, "/Organization/123%2F567/DeploymentProfile/1%25432", DeploymentProfileURL("123/567", "1%432"))
}
