-- where did "inventory_tracking_method" come from?



select 
jsonb_pretty(
jsonb_build_object('Item',
--  jsonb_build_object('ApplicationData', application_data ),
--  jsonb_build_object('AttributeArray',
--   jsonb_build_object('Attribute',
--    jsonb_build_object('Value', value),
--     jsonb_build_object('ValueLiteral', value_literal )
--   )))
	jsonb_build_object('AutoPay', auto_pay) ||
		jsonb_build_object('BestOfferDetails',
		jsonb_build_object('BestOfferEnabled', best_offer_enabled)) ||
-- 		||
-- 	jsonb_build_object('Charity', 
--   jsonb_build_object('CharityID', charity_id) ||
--   jsonb_build_object('CharityNumber', charity_number) ||
--   jsonb_build_object('DonationPercent', donation_percent))
	jsonb_build_object('BuyItNowPrice', 
		jsonb_build_object('AmountType', buy_it_now_price) || 
		jsonb_build_object('currencyID', buy_it_now_price_currency)) ||
	jsonb_build_object('CategoryBasedAttributesPrefill', category_based_attributes_prefill) ||
	jsonb_build_object('ConditionID', 'condition_id') ||
	jsonb_build_object('Country', country ) ||
	jsonb_build_object('Currency', currency ) ||
  	jsonb_build_object('Description', description ) ||
	jsonb_build_object('DisableBuyerRequirements', disable_buyer_requirements ) ||
	jsonb_build_object('DispatchTimeMax', dispatch_time_max) ||
	jsonb_build_object('GiftIcon', gift_icon) ||
	jsonb_build_object('GiftServices', gift_services) ||
	jsonb_build_object('HitCounter', hit_counter) ||
	jsonb_build_object('IncludeRecommendations', include_recommendations) ||
	jsonb_build_object('ListingType', listing_type) ||
	jsonb_build_object('Location', location) ||
	jsonb_build_object('PayPalEmailAddress', pay_pal_email_address) ||
	jsonb_build_object('PostalCode', postal_code) ||
	jsonb_build_object('PostCheckoutExperienceEnabled', post_checkout_experience_enabled) ||
	jsonb_build_object('PrivateListing', private_listing) ||
	jsonb_build_object('Quantity', quantity) ||
	jsonb_build_object('CODCost', jsonb_build_object('AmountType', cod_cost) ||
	jsonb_build_object('currencyID', cod_cost_currency_id)) ||
	jsonb_build_object('GlobalShipping', global_shipping) ||
	jsonb_build_object('InsuranceDetails',
		jsonb_build_object('AmountType', insurance_fee) ||
		jsonb_build_object('currencyID', insurance_fee_currency_id) ||
		jsonb_build_object('InsuranceOption', insurance_option)) ||
	jsonb_build_object('SkypeContactOption', skype_contact_option) ||
	jsonb_build_object('SkypeEnabled', skype_enabled) ||
	jsonb_build_object('SkypeID', skype_id) ||
	jsonb_build_object('StartPrice',
		jsonb_build_object('AmountType', start_price) ||
		jsonb_build_object('currencyID', start_price_currency_id)) ||
	jsonb_build_object('SubTitle', sub_title) ||
	jsonb_build_object('Title', title) ||
	jsonb_build_object('UseTaxTable', use_tax_table) ||
	jsonb_build_object('BestOfferDetails',
		jsonb_build_object('BestOfferEnabled', best_offer_enabled)) ||
		jsonb_build_object('BuyItNowPrice', buy_it_now_price)
))
from ebay_product.products
left join ebay_product.charity_product
using (item_sku)
left join ebay_product.charities
using (charity_id);

--  jsonb_build_object('BuyerRequirementDetails', buyer_requirement_details
--   jsonb_build_object('LinkedPayPalAccount', linked_pay_pal_account)
--   jsonb_build_object('MaximumBuyerPolicyViolations', maximum_buyer_policy_violations
--    jsonb_build_object('Count', count)
--    jsonb_build_object('Period', period)
--)
--   jsonb_build_object('MaximumItemRequirements', maximum_item_requirements
--    jsonb_build_object('MaximumItemCount', maximum_item_count)
--    jsonb_build_object('MinimumFeedbackScore', minimum_feedback_score)
--)
--   jsonb_build_object('MaximumUnpaidItemStrikesInfo', maximum_unpaid_item_strikes_info
--    jsonb_build_object('Count', count)
--    jsonb_build_object('Period', period)
--)
--   jsonb_build_object('MinimumFeedbackScore', minimum_feedback_score)
--   jsonb_build_object('ShipToRegistrationCountry', ship_to_registration_country)
--   jsonb_build_object('VerifiedUserRequirements', verified_user_requirements
--    jsonb_build_object('MinimumFeedbackScore', minimum_feedback_score)
--    jsonb_build_object('VerifiedUser', verified_user)
--)
--   jsonb_build_object('ZeroFeedbackScore', zero_feedback_score)
--)
--  jsonb_build_object('BuyerResponsibleForShipping', buyer_responsible_for_shipping)
--   jsonb_build_object('currencyID', currency_id,
--),
--  jsonb_build_object('CategoryMappingAllowed', category_mapping_allowed)
--  jsonb_build_object('Charity', charity
--)
--  jsonb_build_object('ConditionDescription', condition_description)
--  jsonb_build_object('ConditionID', condition_id)
--  jsonb_build_object('CrossBorderTrade', cross_border_trade)
-- 
--  jsonb_build_object('DigitalGoodInfo', digital_good_info
--   jsonb_build_object('DigitalDelivery', digital_delivery)
--)
--  jsonb_build_object('DiscountPriceInfo', discount_price_info
--   jsonb_build_object('MadeForOutletComparisonPrice', made_for_outlet_comparison_price
--    jsonb_build_object('currencyID', currency_id)
--    jsonb_build_object('MinimumAdvertisedPrice', minimum_advertised_price
--     jsonb_build_object('currencyID', currency_id)
--     jsonb_build_object('MinimumAdvertisedPriceExposure', minimum_advertised_price_exposure)
--     jsonb_build_object('OriginalRetailPrice', original_retail_price
--      jsonb_build_object('currencyID', currency_id)
--      jsonb_build_object('SoldOffeBay', sold_offe_bay)
--      jsonb_build_object('SoldOneBay', sold_one_bay)
--)
--     jsonb_build_object('eBayNowEligible', e_bay_now_eligible)
--     jsonb_build_object('eBayPlus', e_bay_plus)
--     jsonb_build_object('ExtendedSellerContactDetails', extended_seller_contact_details
--      jsonb_build_object('ClassifiedAdContactByEmailEnabled', classified_ad_contact_by_email_enabled)
--      jsonb_build_object('ContactHoursDetails', contact_hours_details
--       jsonb_build_object('Hours1AnyTime', hours1_any_time)
--       jsonb_build_object('Hours1Days', hours1_days)
--       jsonb_build_object('Hours1From', hours1_from)
--       jsonb_build_object('Hours1To', hours1_to)
--       jsonb_build_object('Hours2AnyTime', hours2_any_time)
--       jsonb_build_object('Hours2Days', hours2_days)
--       jsonb_build_object('Hours2From', hours2_from)
--       jsonb_build_object('Hours2To', hours2_to)
--       jsonb_build_object('TimeZoneID', time_zone_id)
--)
--)
-- 
--     jsonb_build_object('ItemCompatibilityList', item_compatibility_list
--      jsonb_build_object('Compatibility', compatibility
--       jsonb_build_object('CompatibilityNotes', compatibility_notes)
--       jsonb_build_object('NameValueList', name_value_list
--        jsonb_build_object('Name', name)
--        jsonb_build_object('Value', value)
-- 
--)
-- 
--)
-- 
--)
--     jsonb_build_object('ItemSpecifics', item_specifics
--      jsonb_build_object('NameValueList', name_value_list
--       jsonb_build_object('Name', name)
--       jsonb_build_object('Value', value)
-- 
--)
-- 
--)
--     jsonb_build_object('ListingCheckoutRedirectPreference', listing_checkout_redirect_preference
--      jsonb_build_object('ProStoresStoreName', pro_stores_store_name)
--      jsonb_build_object('SellerThirdPartyUsername', seller_third_party_username)
--)
--     jsonb_build_object('ListingDesigner', listing_designer
--      jsonb_build_object('LayoutID', layout_id)
--      jsonb_build_object('OptimalPictureSize', optimal_picture_size)
--      jsonb_build_object('ThemeID', theme_id)
--)
--     jsonb_build_object('ListingDuration', listing_duration)
--     jsonb_build_object('ListingEnhancement', listing_enhancement)
-- 
--     jsonb_build_object('ListingSubtype2', listing_subtype2)
--     jsonb_build_object('LiveAuction', live_auction)
--     jsonb_build_object('LotSize', lot_size)
--     jsonb_build_object('MotorsGermanySearchable', motors_germany_searchable)
--     jsonb_build_object('PaymentDetails', payment_details
--      jsonb_build_object('DaysToFullPayment', days_to_full_payment)
--      jsonb_build_object('DepositAmount', deposit_amount
--       jsonb_build_object('currencyID', currency_id)
--       jsonb_build_object('DepositType', deposit_type)
--       jsonb_build_object('HoursToDeposit', hours_to_deposit)
--)
--      jsonb_build_object('PaymentMethods', payment_methods)
-- 
--      jsonb_build_object('PickupInStoreDetails', pickup_in_store_details
--       jsonb_build_object('EligibleForPickupDropOff', eligible_for_pickup_drop_off)
--       jsonb_build_object('EligibleForPickupInStore', eligible_for_pickup_in_store)
--)
--      jsonb_build_object('PictureDetails', picture_details
--       jsonb_build_object('GalleryDuration', gallery_duration)
--       jsonb_build_object('GalleryType', gallery_type)
--       jsonb_build_object('GalleryURL', gallery_url)
--       jsonb_build_object('PhotoDisplay', photo_display)
--       jsonb_build_object('PictureURL', picture_url)
-- 
--)
--      jsonb_build_object('PrimaryCategory', primary_category
--       jsonb_build_object('CategoryID', category_id)
--)
--      jsonb_build_object('ProductListingDetails', product_listing_details
--       jsonb_build_object('BrandMPN', brand_mpn
--        jsonb_build_object('Brand', brand)
--        jsonb_build_object('MPN', mpn)
--)
--       jsonb_build_object('EAN', ean)
--       jsonb_build_object('IncludeeBayProductDetails', includee_bay_product_details)
--       jsonb_build_object('IncludeStockPhotoURL', include_stock_photo_url)
--       jsonb_build_object('ISBN', isbn)
--       jsonb_build_object('ProductID', product_id)
--       jsonb_build_object('ProductReferenceID', product_reference_id)
--       jsonb_build_object('ReturnSearchResultOnDuplicates', return_search_result_on_duplicates)
--       jsonb_build_object('TicketListingDetails', ticket_listing_details
--        jsonb_build_object('EventTitle', event_title)
--        jsonb_build_object('PrintedDate', printed_date)
--        jsonb_build_object('PrintedTime', printed_time)
--        jsonb_build_object('Venue', venue)
--)
--       jsonb_build_object('UPC', upc)
--       jsonb_build_object('UseFirstProduct', use_first_product)
--       jsonb_build_object('UseStockPhotoURLAsGallery', use_stock_photo_urlas_gallery)
--)
--      jsonb_build_object('QuantityInfo', quantity_info
--       jsonb_build_object('MinimumRemnantSet', minimum_remnant_set)
--)
--      jsonb_build_object('ReservePrice', reserve_price jsonb_build_object('currencyID',)
--       jsonb_build_object('ReturnPolicy', return_policy
--        jsonb_build_object('EAN', ean)
--        jsonb_build_object('ExtendedHolidayReturns', extended_holiday_returns)
--        jsonb_build_object('RefundOption', refund_option)
--        jsonb_build_object('RestockingFeeValueOption', restocking_fee_value_option)
--        jsonb_build_object('ReturnsAcceptedOption', returns_accepted_option)
--        jsonb_build_object('ReturnsWithinOption', returns_within_option)
--        jsonb_build_object('ShippingCostPaidByOption', shipping_cost_paid_by_option)
--        jsonb_build_object('WarrantyDurationOption', warranty_duration_option)
--        jsonb_build_object('WarrantyOfferedOption', warranty_offered_option)
--        jsonb_build_object('WarrantyTypeOption', warranty_type_option)
--)
--       jsonb_build_object('ScheduleTime', schedule_time)
--       jsonb_build_object('SecondaryCategory', secondary_category
--        jsonb_build_object('CategoryID', category_id)
--)
--       jsonb_build_object('Seller', seller
--        jsonb_build_object('MotorsDealer', motors_dealer)
--)
--       jsonb_build_object('SellerContactDetails', seller_contact_details
--        jsonb_build_object('CompanyName', company_name)
--        jsonb_build_object('County', county)
--        jsonb_build_object('Phone2AreaOrCityCode', phone2_area_or_city_code)
--        jsonb_build_object('Phone2CountryCode', phone2_country_code)
--        jsonb_build_object('Phone2LocalNumber', phone2_local_number)
--        jsonb_build_object('PhoneAreaOrCityCode', phone_area_or_city_code)
--        jsonb_build_object('PhoneCountryCode', phone_country_code)
--        jsonb_build_object('PhoneLocalNumber', phone_local_number)
--        jsonb_build_object('Street', street)
--        jsonb_build_object('Street2', street2)
--)
--       jsonb_build_object('SellerInventoryID', seller_inventory_id)
--       jsonb_build_object('SellerProfiles', seller_profiles
--        jsonb_build_object('SellerPaymentProfile', seller_payment_profile
-- 	jsonb_build_object('PaymentProfileID', payment_profile_id)
-- 	jsonb_build_object('PaymentProfileName', payment_profile_name)
--)
--        jsonb_build_object('SellerReturnProfile', seller_return_profile
-- 	jsonb_build_object('ReturnProfileID', return_profile_id)
-- 	jsonb_build_object('ReturnProfileName', return_profile_name)
--)
--        jsonb_build_object('SellerShippingProfile', seller_shipping_profile
-- 	jsonb_build_object('ShippingProfileID', shipping_profile_id)
-- 	jsonb_build_object('ShippingProfileName', shipping_profile_name)
--)
--)
--       jsonb_build_object('SellerProvidedTitle', seller_provided_title)
--       jsonb_build_object('ShippingDetails', shipping_details
--        jsonb_build_object('CalculatedShippingRate', calculated_shipping_rate
-- 	jsonb_build_object('InternationalPackagingHandlingCosts', international_packaging_handling_costs
-- 	 jsonb_build_object('currencyID', currency_id)
-- 	 jsonb_build_object('MeasurementUnit', measurement_unit)
-- 	 jsonb_build_object('OriginatingPostalCode', originating_postal_code)
-- 	 jsonb_build_object('PackageDepth', package_depth
-- 	  jsonb_build_object('measurementSystem', measurement_system)
-- 	  jsonb_build_object('PackageLength', package_length
-- 	   jsonb_build_object('measurementSystem') measurement_system
-- 	   jsonb_build_object('PackageWidth ' package_width,
-- 	    jsonb_build_object('measurementSystem', measurement_system)
-- 	   jsonb_build_object('PackagingHandlingCosts', packaging_handling_costs
-- 	    jsonb_build_object('currencyID', currency_id)
-- 	   jsonb_build_object('ShippingIrregular', shipping_irregular)
-- 	   jsonb_build_object('ShippingPackage', shipping_package)
-- 	    jsonb_build_object('WeightMajor ' weight_major,
-- 	     jsonb_build_object('measurementSystem', measurement_system)
-- 	     jsonb_build_object('WeightMinor ' weight_minor,
-- 	      jsonb_build_object('measurementSystem', measurement_system)
--)
-- 	     jsonb_build_object('ExcludeShipToLocation', exclude_ship_to_location)
-- 
-- 	     jsonb_build_object('InternationalInsuranceDetails', international_insurance_details
-- 	      jsonb_build_object('InsuranceFee', insurance_fee
-- 	       jsonb_build_object('currencyID', currency_id))
-- 	      jsonb_build_object('InsuranceOption', insurance_option)
--)
-- 	     jsonb_build_object('InternationalPromotionalShippingDiscount', international_promotional_shipping_discount)
-- 	     jsonb_build_object('InternationalShippingDiscountProfileID', international_shipping_discount_profile_id)
-- 	     jsonb_build_object('InternationalShippingServiceOption', international_shipping_service_option
-- 	      jsonb_build_object('InternationalShippingServiceOptionsType', international_shipping_service_options_type
-- 	      jsonb_build_object('ShippingService', shipping_service)
-- 	       jsonb_build_object('ShippingServiceAdditionalCost', shipping_service_additional_cost
-- 		jsonb_build_object('currencyID', currency_id))
-- 	       jsonb_build_object('ShippingServiceCost', shipping_service_cost
-- 		jsonb_build_object('currencyID', currency_id))
-- 	      jsonb_build_object('ShippingServicePriority', shipping_service_priority)
-- 	      jsonb_build_object('ShipToLocation', ship_to_location)
-- 
--)
-- 
-- 	     jsonb_build_object('PaymentInstructions', payment_instructions)
-- 	     jsonb_build_object('PromotionalShippingDiscount', promotional_shipping_discount)
-- 	      jsonb_build_object('RateTableDetails', rate_table_details
-- 	      jsonb_build_object('DomesticRateTable', domestic_rate_table)
-- 	      jsonb_build_object('InternationalRateTable', international_rate_table)
--)
-- 	     jsonb_build_object('SalesTax', sales_tax
-- 	      jsonb_build_object('SalesTaxPercent', sales_tax_percent)
-- 	      jsonb_build_object('SalesTaxState', sales_tax_state)
-- 	      jsonb_build_object('ShippingIncludedInTax', shipping_included_in_tax)
--)
-- 	     jsonb_build_object('ShippingDiscountProfileID', shipping_discount_profile_id)
-- 	     jsonb_build_object('ShippingServiceOptions', shipping_service_options
-- 	      jsonb_build_object('FreeShipping', free_shipping)
-- 	      jsonb_build_object('ShippingService', shipping_service)
-- 	      jsonb_build_object('ShippingServiceAdditionalCost', shipping_service_additional_cost
-- 	       jsonb_build_object('currencyID', currency_id))
-- 	      jsonb_build_object('ShippingServiceCost', shipping_service_cost
-- 	       jsonb_build_object('currencyID', currency_id))
-- 	      jsonb_build_object('ShippingServicePriority', shipping_service_priority)
-- 	      jsonb_build_object('ShippingSurcharge', shipping_surcharge
-- 	       jsonb_build_object('currencyID', currency_id))
--)
-- 
-- 	     jsonb_build_object('ShippingType', shipping_type)
--)
-- 	    jsonb_build_object('ShippingPackageDetails', shipping_package_details
-- 	     jsonb_build_object('MeasurementUnit', measurement_unit)
-- 	     jsonb_build_object('PackageDepth ' package_depth,
-- 	      jsonb_build_object('measurementSystem', measurement_system)
-- 	      jsonb_build_object('PackageLength ' package_length,
-- 	       jsonb_build_object('measurementSystem', measurement_system)
-- 	       jsonb_build_object('PackageWidth ' package_width,
-- 		jsonb_build_object('measurementSystem', measurement_system)
-- 		jsonb_build_object('ShippingIrregular', shipping_irregular)
-- 		jsonb_build_object('ShippingPackage', shipping_package)
-- 		jsonb_build_object('WeightMajor ' weight_major,
-- 		 jsonb_build_object('measurementSystem', measurement_system)
-- 		 jsonb_build_object('WeightMinor ' weight_minor,
-- 		  jsonb_build_object('measurementSystem', measurement_system)
--)
-- 		 jsonb_build_object('ShippingServiceCostOverrideList',
-- 		  jsonb_build_object('ShippingServiceCostOverride', shipping_service_cost_override
-- 		   jsonb_build_object('ShippingServiceAdditionalCost', shipping_service_additional_cost
-- 		    jsonb_build_object('currencyID', currency_id))
-- 		   jsonb_build_object('ShippingServiceCost', shipping_service_cost
-- 		    jsonb_build_object('currencyID', currency_id))
-- 		   jsonb_build_object('ShippingServicePriority', shipping_service_priority)
-- 		   jsonb_build_object('ShippingServiceType', shipping_service_type)
-- 		   jsonb_build_object('ShippingSurcharge', shipping_surcharge
-- 		    jsonb_build_object('currencyID', currency_id))
--)
-- 
--)
-- 		 jsonb_build_object('ShippingTermsInDescription', shipping_terms_in_description)
-- 		 jsonb_build_object('ShipToLocations', ship_to_locations)
-- 
-- 		 jsonb_build_object('Site', site)
-- 		 jsonb_build_object('SKU', sku)
-- 		  jsonb_build_object('currencyID', currency_id))
-- 		 jsonb_build_object('Storefront', storefront
-- 		  jsonb_build_object('StoreCategory2ID', store_category2_id)
-- 		  jsonb_build_object('StoreCategory2Name', store_category2_name)
-- 		  jsonb_build_object('StoreCategoryID', store_category_id)
-- 		  jsonb_build_object('StoreCategoryName', store_category_name)
--)
-- 		 jsonb_build_object('TaxCategory', tax_category)
-- 		 jsonb_build_object('ThirdPartyCheckout', third_party_checkout)
-- 		 jsonb_build_object('ThirdPartyCheckoutIntegration', third_party_checkout_integration)
-- 		 jsonb_build_object('UseRecommendedProduct', use_recommended_product)
-- 		 jsonb_build_object('UUID', uuid)
--)
-- 
-- 		jsonb_build_object('ErrorHandling', error_handling)
-- 		jsonb_build_object('ErrorLanguage', error_language)
-- 		jsonb_build_object('MessageID', message_id)
-- 		jsonb_build_object('Version', version)
-- 		jsonb_build_object('WarningLevel', warning_level)
--)
-- from ebay_product.products;
