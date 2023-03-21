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

const (
	// PaymentMethod types
	// Used in PaymentProvider.type & PaymentMethod.type.

	// PaymentMethodTypeCreditCard indicates that the payment method
	// is of type creditcard.
	PaymentMethodTypeCreditCard = "creditcard"
	// PaymentMethodTypeInternalCredit indicates that the payment method
	// is of type credit.
	PaymentMethodTypeInternalCredit = "credit"
)

const (
	// Credit card types
	// Used in PaymentMethod.CreditCardInfo.card_type;

	// CardTypeVisa indicates a VISA creditcard
	CardTypeVisa = "visa"
	// CardTypeMastercard indicates a Mastercard creditcard
	CardTypeMastercard = "mastercard"
)
