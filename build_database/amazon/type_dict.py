type_dict = {
'An alphanumeric string detailing the size of the product that a customer would select when purchasing.  E.g. Small, Medium, Large.  For items that do not vary by size, simply state “One Size”.': 'varchar',

'Select: lumens': 'varchar',

'Industrial standard met by the product (up to 5 standards). Please see Browse Tree Guide and Website for recommended values.': 'varchar',

'An alphanumeric string with a 1-character minimum and 40-character maximum.': 'varchar(40)',

'An alphanumeric string up to a maximum of 100 characters in length.': 'varchar(100)',

'An alphanumeric string; 1 character minimum in length and 100 characters maximum in length.':  'varchar(100)',

'Select one of the following options: manual, power.': 'varchar',

'Hard, Extra Hard': 'varchar',

'Select a value from:\nFT\nM': 'varchar',

'Use the column FillMaterialType in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Select one of the following options: milliamps or amps. Please do not include the actual amperage, which will be collected in the amperage field.': 'varchar',

'Select a value from the Valid Values worksheet.': 'varchar',

'An alphanumeric text string; 1 character minimum and 50 characters maximum. Also See Valid Values.': 'varchar(50)',

'Select an item type value from the Valid Values sheet.': 'varchar',

'For what activities, events, locations, or conditions is the product intended to be used?': 'varchar',

'Text - maximum 50 characters. HTML tags and special characters not on a standard keyboard (eg. ®, ©, ™ or other Type 1 High ASCII characters) are not supported': 'varchar(50)',
    
'Lumens': 'varchar',

'Manual, Fixed, Vari-focal, Motorized': 'varchar',

'Use this field to indicate if a cautionary statement relating to the choking hazards of children\'s toys and games applies to your product.  These cautionary statements are defined in Section 24 of the Federal Hazardous Substances Act and Section 105 of the Consumer Product Safety Improvement Act of 2008.  They must be displayed on the product packaging and in certain online and catalog advertisements.  You are responsible for determining if a cautionary statement applies to the product.  This can be verified by contacting the product manufacturer or checking the product packaging.   Cautionary statements that you select will be displayed on the product detail page.  If no cautionary statement applies to the product, select "no_warning_applicable".': 'varchar',

'Positive integer, no decimal point': 'int',

'Any string value up to 50 characters.': 'varchar(50)',

'autofocus self-illumination light': 'varchar',

'An alphanumeric string; 50 characters maximum. Please refer to the SpecificUsageForProduct column in the Valid Values tab.': 'varchar(50)',

    "String, max 8 characters, always beginning with 'Class ' followed by up to 2 digits\nClass 10\nClass 4\nClass 2\nClass 6" : 'varchar',

'Must be a positive whole number, less than XXXXX’': 'varchar',

'A whole number.': 'int',

'Select from the following Valid Values:\nblues \ngospel \ncountry \ndance \nfolk \njazz \nnew-age \npop \nr-and-b \nrap-and-hip-hop \nrock \nworld-music': 'varchar',

'Use the column NeckStyle in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

    'A positive integer with up to 10 digits.': 'int',
 
'A text string with a 2,000-character maximum. Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.':  'varchar(2000)',

'A valid URL, including leading "http://"\n\nThe url is case sensitive, so make sure to use matching capitalization and no redirections (e.g. .jpeg instead of .jpg). While a web browser might be smart enough to locate your image despite of these little inaccuracies, our image collection process isn\'t.': 'varchar',

'Select from the following valid values:\nlp\n12_single\n45\nep\n78\nother\nunknown': 'varchar',

'Alphabetical free text; 1 character minimum in length and 50 characters maximum in length.': 'varchar(50)',

'A positive integer. Accepted unit of measure is watt.': 'int',

'Selected from the dropdown list.': 'varchar',

'fixed, vari-focal, motorized zoom': 'varchar',

'Select: Single, Dual or Dual Selectable': 'varchar',

'Any whole number between 150 and 185.': 'int',

'ip network, analog': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas.\n\nThe accepted unit of measure for this attribute is: GB': 'numeric(10, 2)',

'Ethernet, Wireless, Powerline, USB, RJ11': 'varchar',

'The product\'s medium or format"': 'varchar',

'Text; 2,000 characters maximum length. Note: ASCII characters (®, ©, ™, etc.) and other special characters are not supported.': 'varchar(2000)',

'Methods for connecting to or from this device': 'varchar',

    'The wattage rating of the product. Input a number only--do not enter units.': 'int',

    'Positive Integer': 'int',

'An alphanumeric string up to 100 characters.': 'varchar(100)',

'Select applicable special feature values from the Valid Values sheet.': 'varchar',

'Select from the following valid values: \nIN\nFT\nMM\nCM\nM': 'varchar',

'The main materials used in the product': 'varchar',

'Select a value from the Valid Values worksheet': 'varchar',

'An alphanumeric string; 1 character minimum in length and 50 characters maximum in length.\n\nYou must include either UPC or manufacturer plus mfr-part-number.': 'varchar(50)',

'automatic, manual, manual-and-auto, focus-free': 'varchar',

'A text field.': 'varchar',

'Alphanumeric string max 50 characters': 'varchar(50)',

    'The number of audio channels the receiver will support': 'int',

'An alphanumeric string; 1 character minimum in length and 50 characters maximum in length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.':  'varchar(50)',

'Positive integer, max 3 digits to the left and 2 to the right of the decimal point': 'numeric(3, 2)',

    'A four-digit year.': 'int',

'16mm, 35mm, 70mm, 110, 120, 220, 2x3, 4x5, 5x7, 6x8, 8x10, 8x20, 10x12, 11x14, 12x20, 14x17, 16x20, aps, micro, instant, other': 'varchar',

'Please select from the following: Fabric\nFaux shearling or fur\nGore-Tex\nLeather\nLeather and synthetic\nMesh\nShearling or fur\nSynthetic\nUnknown': 'varchar',

'Indicates the time, in days, between when you receive an order for an item and when you can ship the item.\xa0 The default is one to two business days. Use this field if you expect to take longer than two business days. ': 'int',

'Use the column SkillLevel in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar',

    "Select the appropriate value.  If you have Macro's turned on just select the correct value.  If you have Macro's turned off please copy and paste the correct League Name from the Valid Values tab." : 'varchar',

    'Is autographed?' : 'varchar',

'A date in this format: MM-DD-YYYY': 'date',

'Images should have 72-pixels-per-inch resolution and be 500 pixels minimum in length (on the longest side). The preferred file format is JPEG (.jpg). When naming your image, please use the following convention: Product SKU + View Indicator (i.e., .main) + File Extension (i.e., .jpg). An example would be: "15774.main.jpg". Save the image to your Web server and supply the URL to the image in this field. There cannot be any spaces or high ascii characters in the image url.':  'varchar',

'A positive integer. Accepted unit of measure is watts.': 'int',

'Select: Fan LED indicator or leave blank': 'varchar',

'true, false': 'varchar',

'AC, DC, Battery, AC & Battery, Solar, Fuel Cell, Kinetic': 'varchar',

'A number with up to 10 digits allowed to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas.': 'numeric(10, 2)',

'Select: NVIDIA or ATI': 'varchar',

'Thread Coverage': 'varchar',

    "Select the appropriate value.  If you have Macro's turned on just select the correct value.  If you have Macro's turned off please copy and paste the correct Jersey Type from the Valid Values tab." : 'varhcar',

'An alphanumeric string with a 500-character maximum per bullet point. Please do not include an actual bullet point object, just the text used to describe your product. Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.' : 'varchar',

'Bluetooth, RF, IR, Wi-Fi, Airplay, VHF, UHF, AM, FM, AM/FM, Shortwave, 3G, 4G, GPRS, GSM': 'varchar',

'Please refer to the Valid Values tab.': 'varchar',

'A text string; 2,000 characters maximum in length.':  'varchar(2000)',

'The energy certifications that the product has': 'varchar',

'Use the column Season in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'A text string, 1,000 characters maximum in length.': 'varchar(1000)',

'Select one of the following options: True or False': 'varchar',

'An alphanumeric string; 1 character minimum in length and 1500 characters maximum in length.': 'varchar(1500)',

'Select one of the following options: GR, KG, OZ, or LB.': 'varchar',

'An alphanumeric string; 1 character minimum in length and 50 characters maximum in length.\n': 'varchar(50)',

'Wired, Wireless': 'varchar',

'Please select the correct Item Type from the Browse Tree Guide (BTG)': 'varchar',

'- Minimum 3 and maximum 5 bullet points.\n- Should be written in sentence caps, be short and concise and give the customer a good overview of the product\n- An alphanumeric string; 100 characters maximum length per bullet point. Do not include ponctuation at the end of the bullet point\n- Please do not include an actual bullet point object, just the text used to describe your product. \n- Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(100)',

'Use the column DepartmentName in the Valid Values list.': 'varchar',

'Select one of the following options: true or false': 'varchar',

'Select one of the following options: \nworld-instruments\nartist-signature-series\nleft-handed': 'varchar',

'Select from valid values list': 'varchar',

'An alphanumeric string; 1 character minimum in length and 500 character maximum in length.': 'varchar(500)',

'TV, Wall, Ceiling, Speaker': 'varchar',

'Select from a list of valid values': 'varchar',

'Text - maximum 20 characters. HTML tags and special characters not on a standard keyboard (eg. ®, ©, ™ or other Type 1 High ASCII characters) are not supported': 'varchar(20)',

'WMA, AAC, FLAC, MP3': 'varchar',

    'For MAP (Minimum Advertised Price) based pricing.  If you have never heard this term before, this function probably does not apply to you.': 'numeric',

'The base color with which an item is associated.': 'varchar',

'Provide specific search terms to help customers find your product.': 'varchar',

'Select one of the following options: cubic-cm, cubic-ft, cubic-in, cubic-m, cubic-yd, cup, gallon, liter, ounce, pint, quart. Do not include the actual volume, which will be collected in the volume field.': 'varchar',

'You can place your listings on sale by entering a sale price (expressed in local currency) along with start and end dates.': 'numeric',

'The year this product was released, expressed as (YYYY).': 'int',

'The region encoding, usually specified on the back of the video packaging.  Select the appropriate value from the drop-down provided.': 'varchar',

'The screen display type used by the product': 'varchar',

'Use the column CompatibleDevices in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point.  Please do not use commas, but a point as decimal separator. Will only be displayed if item-length, item-width, item-height are filled.': 'numeric(10, 2)',

'Air cooled, Water cooled': 'varchar',

'A number with up to 18 digits allowed to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas or currency symbols.': 'numeric(18, 2)',

'Select: true (if your product is subject to this rule).': 'varchar',

'Number of CDs or tapes included with the product. This is not the quantity you have available for sale': 'varchar',

'Select "Variation"': 'varchar',

'String of text with max of 50 characters': 'varchar(50)',

'An alphanumeric text string; 1 character minimum and 50 characters maximum. If multiple colours are available, a unique record should be submitted for each product.':  'varchar(50)',

'Use the column PowerSource in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'How should your product be categorized?': 'varchar',

'An alphanumeric string; 1 character minimum in length and 1000 characters maximum in length.': 'varchar(1000)',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas.\n\nThe unit of measure is always hours': 'numeric(10, 2)',

'Select: True (if your product is subject to this rule)': 'varchar',

    "Select the appropriate value.  If you have Macro's turned on just select the correct value.  If you have Macro's turned off please copy and paste the correct Website Shipping Weight Unit Of Measure from the Valid Values tab." : 'varchar', 

'If building a variation relationship, select one of the following options: parent or child.\n\nThe product ‘Marilyn Monroe Master Print\' would have the value \"parent\" and the product \"Marilyn Monroe Master Print 11x14 Wood Frame\' would have the value \"child.\"\n': 'varchar',

'The type of standard, unique identifier entered in the Product ID field. This is a required field if Product ID is provided.': 'varchar',

'AMAZON_NA, DEFAULT': 'varchar',

'The name of how the unit of a product is measured in terms of volume (fluid ounces), weight (grams, ounces, pounds), or count.': 'varchar',

'Indicates the type of identifier provided, e.g. ASIN, UPC, EAN, GCID or GTIN.': 'varchar',

'OZ, LB, GR, KG': 'varchar',

'Not currently used in Musical Instruments.': 'varchar',

'not_water_resistant, water_resistant, waterproof': 'varchar',

'choking_hazard_balloon, choking_hazard_contains_a_marble, choking_hazard_contains_small_ball, choking_hazard_is_a_marble, choking_hazard_is_a_small_ball, choking_hazard_small_parts, no_warning_applicable': 'varchar',

'How are the Lithium Batteries packaged?': 'varchar',

'Select a value from the Valid Values worksheet.edition number is usually for nonfiction books, only.  It does not refer to print run or collectible "1st edition" status.  Except in rare cases where the author has actually revised the text and reissued it, fiction books shouldn\'t list edition numbers.': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas,.': 'numeric(10, 2)',

'A positive integer with up to 3 digits.': 'int',

'An alphanumeric string with a 1-character minimum and 100-character maximum. Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.':  'varchar(100)',

'A value provided during the registration process. Do not input a value when not known.': 'varchar',

'Select a used for value from the BTG': 'varchar',

'Select one of the following options:\nactive\npassive': 'varchar',

'The color of the item.': 'varchar',

'touch_screen': 'varchar',

'A positive integer.\n': 'int',

'Positive integer, max 6 digits, no decimal point': 'int',

'cable, ir, radio, universal': 'varchar',

'Voltage of each battery (or cell) in unit expressed in volts.': 'int',

'Use the column MountainBikeType for  in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Specify if the manufacturer is providing a warranty on this product.': 'varchar',

'An alphanumeric string assigned by the record label, usually appearing on the product label or packaging': 'varchar',

'Integer.': 'int',

'An alphanumeric string; 1 character minimum in length and 50 characters maximum in length.': 'varchar(50)',

'Either a decimal value, or a one of the following options:\nAnkle\nMid-Calf\nKnee-High\nOver-the-Knee': 'varchar',

'A text string; 50 characters maximum in length.': 'varchar(50)',

'String': 'varchar',

'A positive whole number. Please do not include the word "watts."': 'int',

'psi, Newton': 'varchar',

    "4-digit number (e.g., '2011')" : 'int', 

    'MM (for millimeters)':  'varchar',

'A positive number.': 'int',

'JPEG, RAW, CANON_RAW': 'varchar',

'Select from the following valid values:\ncup\ngallon\nliter\nounce': 'varchar',

'See Valid Values Tab': 'varchar',

'Use the column SupportType in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Number; assumed to be in seconds (s)': 'int',

'ac, dc, lead-acid-battery, lithium-battery, lithium-ion-battery, nickel-metal-hydride-battery, nicd-battery, silver-oxide-battery, alkaline-battery, other-battery-types': 'varchar',

'A text string up to 50 characters.': 'varchar(50)',

'Select one of the following:\nAerosols\nFlammables\nOxidisers\nRestricted Hazmat': 'varchar',

'Select one Of the following options:\nMicrophone\nFM Transmitter\nStereo\nWind Noise Reduction\nNoise Cancellation\nPC Calling': 'varchar',

'A comma-delimited list including any combination of the following:\n\n"Next" (One day)\n"Second" (Two day)\n"Domestic" (Domestic Expedited)\n"International" (International Expedited)\n"Plus" (Faster Expedited Domestic: 1 to 3 days. Eligibility based on performance. See "Learn More" link below.)\n\nN = None, no expedited shipping offered': 'varchar',

'The year this product was originally released, expressed as (YYYY).': 'int',

'Positive integer, no decimal point, at most 10 digits': 'int',

'AM, FM, AM/FM, HD Radio, Satellite, Internet Radio': 'varchar',

'Select one of the following options: GR, KG, OZ or LB. Do not include the actual weight, which will be collected in the ShippingWeight field.': 'varchar',

'An alphanumeric string up to a maximum of 50 characters in length.': 'varchar(50)',

    "No restrictions - since it's the features of the product they can enter whatever they would like." : 'varchar', 

    "Any string value up to 200 characters; separate different contributors' name using a semicolon." : 'varchar(200)', 

'Select from a list of valid values\n' : 'varchar',

'Please refer to the BTG.': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point.': 'numeric(10, 2)',

'Select one of the following options: CM, M, IN, or FT. Do not include the actual measurements; these will be collected in the item-length, item-width, and item-height fields.': 'varchar',

'PrivateLabel, Specialized, NonConsumer, or PreConfigured.': 'varchar',

'tabletop, travel, hiking-and-outdoors, hunting-and-shooting or sports, marine': 'varchar',

'The size of the screen measured diagonally': 'varchar',

'A whole number between 1 and 16': 'int',

'Select one of the following options: \n\nchoking_hazard_balloon\nchoking_hazard_contains_a_marble\nchoking_hazard_contains_small_ball\nchoking_hazard_is_a_marble\nchoking_hazard_is_a_small_ball\nchoking_hazard_small_parts\nno_warning_applicable': 'varchar',

'Use the column CollarType in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Select from the following valid values: \nLB\nOZ\nKG': 'varchar',

'Select one of the following options: With Case, With Bag, or Not Included.': 'varchar',

'Enter an alphabetic string of up to 50 characters maximum length.': 'varchar(50)',

' Select a value from the Valid Values worksheet': 'varchar',

'Select one of the following options: \ndecimeters\nmillimeters\ncentimeters\ninches': 'varchar',

'Indicate the width of the item.': 'int',

'The weight in original package': 'int',

'Select one of the following options:\n\nLBS\nKG': 'varchar',

    "Max. 100 characters per line. Use these to highlight some of the product's most important qualities. Each line will be displayed as a separate bullet point above the product description." : 'varchar(100)',

'Please refer to the  Browse Tree Guide (BTG).' : 'varchar(100)',

'An alphanumeric string; 1 character minimum in length and 500 characters maximum in length per entry.': 'varchar(500)',

'This is the date when you can deliver a pre-orderable product (one that has never been available prior to this date) to a customer.': 'date',

'Select one of the following options: Square foot, Roll': 'varchar',

'Free text with up to 500 characters.  Please use correct syntax.': 'varcar(500)',

'An alphanumeric string; 500 characters maximum in length.': 'varchar(500)',

'Select "Game Used" (if your product is subject to this rule). If your product is not game used, select "Not Game Used"': 'varchar',

'A number with up to 4 digits, reflecting the runtime in minutes.': 'int',

'Can be text or a number with the unit of measure included.': 'varchar',

'A date in this format: yyyy/mm/dd.': 'date',

'Accepted units of measure are MHz, GHz.': 'varchar',

'Select one of the following options: Over-The-Ear\nBehind-The-Ear\nIn-The-Ear': 'varchar',

'The watts per channel, entered as a whole number.': 'int',

'Provide only information that describes the features of the product in general and not information that is specific to your particular offer (for example: do not provide item condition, shipping or promotional information': 'varchar',

'An alphanumeric string with a 1-character minimum and 500-character maximum. Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(500)',

'A whole number between 1 and 15': 'int',

'Auto-reject customer offers within the discount range.': 'varchar',

'An alphanumeric text string; 50 characters maximum. If multiple scents are available, a unique record should be submitted for each product.': 'varchar(50)',

'Please see listing requirements here: https://sellercentral.amazon.com/gp/help/50211': 'varchar',

'Select one of the following options: MM, CM, M, IN, FT': 'varchar',

'Select one of the following options: \nCM or IN.': 'varchar',

'Select a value from the StrapType column in the Valid Values tab.': 'varchar',

'A positive integer.  The unit of measure is pages-per-minute': 'int',

'Blu-ray, VHS, Cassette, DVD, CD': 'varchar',

'A text string; 1,000 characters maximum in length.': 'varchar(1000)',

'Select one of the following options: GR, KG, OZ, LB': 'varchar',

'CM, M, IN, or FT. Do not include the actual measurements; these will be collected in the item-length, item-width, and item-height fields.': 'varchar',

'Please refer to the Valid Values sheet': 'varchar',

'Select the appropriate language from the drop-down provided.': 'varchar',

'A whole number with 4 digits.': 'int',

'Images should have 72-pixels-per-inch resolution and be 1001 pixels minimum in length (on the longest side). The preferred file format is JPEG (.jpg), and the URL must be fully-formed and valid (i.e., include http://). When naming your image, you may use the following convention (though not required): Product SKU + View Indicator (.main) + File Extension (.jpg). An example would be: "15774.main.jpg".  There cannot be any spaces or high ascii characters in the image url.  Save the image to your Web server and supply the URL to the image in this field.  Accepted formats are .jpeg, .jpg, and .gif Refer to the Image Info tab for more information.': 'varchar',

'"1" or "n"  = Will ship within the marketplace only\n"2" or "y" = Will ship to international locations': 'varchar',

'Select one of the following options: Global Catalog ID (GCID), UPC, EAN or GTIN': 'varchar',

'Text; 500 characters maximum length': 'varchar(500)',

'Select: Analog or Digital': 'varchar',

'Please choose from the following choices:\nblack, blue, bronze, brown, gold, gray, green, metallic, off-white, orange, pink, purple, red, silver, white, yellow': 'varchar',

'Wood, Metal, Plastic, Composite': 'varchar',

'This is the weight in gms of lithium contained in each "metal" cell or battery or in the case of rechargeable batteries it is the "equivilent lithium content" expressed in grams, in each ion cell or battery.': 'varchar',

'Grade': 'varchar',

'Positive decimal, with up to 5 digits to the left and 2 to the right of the decimal point': 'numeric(5, 2)',

'Select from list of valid values and reference the BTG': 'varchar',

'geared-heads, ball-heads, camera-rotator-heads, pan-and-tilt-heads, video-heads, 3-way-heads, panoramic-heads': 'varchar',

'Color names': 'varchar',

'Select a target audience value from the BTG': 'varchar',

'A number with up to 10 digits allowed to the left of the decimal point and 2 digits allowed to the right of the decimal point. Please do not use commas or dollar signs.': 'numeric(10, 2)',

'String, max 20 characters': 'varchar(20)',

'The average life of the battery, in hours.': 'int',

'Use the column GradingBy in the Valid Values list. An alphanumeric string; 50 characters maximum. If blank, the Seller will be the default': 'varchar(50)',

'Number; up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas.': 'numeric(10, 2)',

'Use Valid Values column ClosureType. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'batteries_only, batteries_contained_in_equipment, batteries_packed_with_equipment': 'varchar',

'Select one of the following options:\nXXXXX-Small\nXXXX-Small\nXXX-Small\nXX-Small\nX-Small\nSmall\nMedium\nLarge\nX-Large\nXX-Large\nXXX-Large\nXXXX-Large\nXXXXX-Large': 'varchar',

'An alphanumeric string with a 1-character minimum and 50-character maximum.': 'varchar(50)',

'An alphanumeric string, 25 characters in length': 'varchar(25)',

'2.4 Gigahertz, 5.8 Gigahertz, 900 Megahertz, Digital, Analog, Digital Spread Spectrum': 'varchar',

'Any integer greater than or equal to zero': 'int',

'Select from the following valid values: \nKG\nGR\nOZ\nLB': 'varchar',

'Select an applicable variation theme.': 'varchar',

'A positive integer. Accepted unit of measure is wattage': 'int',

'An alphanumeric text string; 1 character minimum and 50 characters maximum. If multiple colors are available, a unique record should be submitted for each product.': 'varchar(50)',

'The name of the music label that released this product': 'varchar',

'Please select a value from the Valid Values tab': 'varchar',

    "This is a true/false field.\n[Default is 'false' if you enter no data.]" : 'varchar',

'Use the column CountryOfOrigin in the Valid Values list. An alphanumeric string; 2 characters maximum.': 'varchar',

'kilograms, grams, milligrams, pounds, ounces': 'varchar',

'GR, KG, OZ, or LB. Do not include the actual weight, which will be collected in the item-weight field.': 'varchar',

'A positive whole number. The unit "Volts" will be appended to the value automatically, so that a value of 120 will display as 120V.': 'int',

'An alphanumeric string; 1 character minimum in length and 100 characters maximum in length. \n\nNote: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar',

'single, dual': 'varchar',

'Select one of the following:\nShelf Life\nExpiration Date Required': 'varchar',

'This attribute will determine if the collectible is original or is reproduced.': 'varchar',

'Select one of the following options: GallonsPerMinute, GallonsPerHour, GallonsPerFlush': 'varchar',

'A positive integer with up to 2 digits.': 'int',

'ccd, 3-chip-ccd, cmos, progressive-scan-ccd, aps-c, super-ccd': 'varchar',

'The country from which the product was legally released.': 'varchar',

'A positive whole number - please do not use fractions/decimals': 'int',

'Select from the following valid values: \nOZ\nLB\nGR\nKG': 'varchar',

'Not Currently Used in Home': 'varchar',

'A whole number between 1 and 18': 'int',

'For Collectible Cards, specify the rarity.': 'varchar',

'Any number in millimeters (mm)': 'int',

'You must select any applicable warning for choking hazards of children’s toys and games, or "no_warning_applicable". To verify warnings, contact the manufacturer or check the packaging.': 'varchar',

'Select from the list of valid values': 'varchar',

'Use the column LensMaterial in the Valid Values list.. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Select one of the following options: \nPrivateLabel\nSpecialized\nNonConsumer\nPreConfigured': 'varchar',

    "Select the appropriate value.  If you have Macro's turned on just select the correct value.  If you have Macro's turned off please copy and paste the correct Team Name from the Valid Values tab." : 'varchar',

    'Select one of the following options: Parent or Child\n\nFor stand alone items, the Parentage needs to be populated with the term "Child".': 'varchar',

'An alphanumeric string; 40 characters maximum in length.\n\nYou must include either UPC or manufacturer plus mfr-part-number.': 'varchar(40)',

'Edition, format and other special features of the record': 'varchar',

'A number with up to 10 digits allowed to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas or dollar signs.': 'numeric(10, 2)',

'Input an approprate product type.': 'varchar',

'A positive integer with up to 12 digits.': 'int',

'This is in addition to the valid values that you must submit for your product.  It is in your best interest to fill in all search terms. Max characters is 50.': 'varchar(50)',

'round, square, bayonet, other': 'varchar',

'An alphanumeric string; 1 character minimum in length and 150 characters maximum in length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(150)',

'Select from the following valid values: \nIN\nCM\nFT': 'varchar',

'Select from the following Valid Values: \nchoking_hazard_balloon\nchoking_hazard_contains_a_marble\nchoking_hazard_contains_small_ball\nchoking_hazard_is_a_marble\nchoking_hazard_is_a_small_ball\nchoking_hazard_small_parts\nno_warning_applicable': 'varchar',

'auto, high speed sync, slow shutter, forced, fill, flash override, red eye reduction': 'varchar',

'indoor, outdoor': 'varchar',

'Select one of the following options: GR, KG, OZ, or LB. Do not include the actual weight, which will be collected in the item-weight field.': 'varchar',

'Alphanumeric string, max 50 characters,': 'varchar(50)',

'Number; assumed to be in inches (in)': 'int',

'Select from the dropdown list.': 'varchar',

'Select one of the following options: LB, OZ, KG, GR': 'varchar',

'Whole numbers with upto 5 digits': 'int',

'The full text of the title as it appears on the product. Include the subtitle if appropriate (separated by a colon). Please do not use all capital letters': 'varchar',

'A positive integer.': 'int',

'Skype, Netflix, Amazon Instant Video, Browser, iTunes, Pandora, Free Sat/Free View, Blockbuster, YouTube, Hulu Plus, Daily Motion, Explore 3D, Vudu, Cinemanow, Google TV': 'varchar',

'A whole positive number.': 'int',

'Please select a valid value from the valid values tab.': 'varchar',

'This attribute is specific for AmazonFresh FBAF merchants. FBAF merchants participate by invitation only.': 'varchar',

'Most products have barcodes (UPC, EAN, etc) that uniquely identify the product. Providing the correct barcode for product listings helps Amazon improve the quality our  catalog and reduce duplicate product listings that confuse customers shopping on Amazon. However, not all products have assigned barcodes. If you are creating custom bundles of 2 or more products, indicate this is a bundle listing by selecting "CustomProductBundle". If you are listing replacement parts that don\'t have barcodes (perhaps only a part number),or you have split a product into component parts not normally sold individually, please select "ReplacementPart". Note for either of these cases you will need to have been previously granted a bundle UPC exemption or replacement part UPC exemption for the brand by Amazon. Leave this column blank for all other types of products.': 'varchar',

'String.  Maximum length 30': 'varchar(30)',

'F, C': 'varchar',

'The date of publication of the product.': 'date',

'Number; assumed to be in Gigabytes (GB)': 'int',

'An alphanumeric string; 1 character minimum in length and 200 character maximum in length.': 'varchar(200)',

'An alphanumeric string; 1 character minimum in length and 500 characters maximum in length. \n\nNote: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(500)',

    "Select the appropriate value.  If you have Macro's turned on just select the correct value.  If you have Macro's turned off please copy and paste the correct Authentication Provided By from the Valid Values tab." : 'varchar',

'any metric, preferably milliliters or millimeters' : 'varchar',

'Select a value from the following:\nGIA\nIGI\nAGS': 'varchar',

'Add your comments about the condition': 'varchar',

'Select an item type value from the BTG': 'varchar',

'Please refer to the Valid Values Sheet . An alphanumeric string; 50 characters maximum.': 'varchar',

'A description of the product, not the condition of your item for sale. Maximum: 2000 characters': 'varchar(200)',

    "What is the product's subject? What is the product about?" : 'varchar',

'Black\nWhite\nTransparent\nBlue\nGreen\nRed\nYellow\nPurple\nOrange\nPink\nBrown\nSilver\nGold\nMulti-coloured': 'varchar',

'Use the column GripMaterialType for  in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Valid values for stonetreatmentmethod:\nHeat-treated\nDyed\nCoated\nImpregnated\nReconstituted\nOiled\nIrradiated\nBleached\nFilled\nLasered\nNot-treated': 'varchar',

'The region encoding, usually specified on the back of the DVD packaging.': 'varchar',

'Positive integer, with up to 10 digits on the left of the decimal point and up to 2 digits on the right of the decimal point, with inches as the unit': 'numeric(10, 2)',

'A text string; 2,000 characters maximum in length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(2000)',

'SD, HDD, MiniDV': 'varchar',

'18H': 'varchar',

'Select from Labor Parts Labor+Parts': 'varchar',

'Text; 500 characters maximum length. Note: ASCII characters (®, ©, ™, etc.) and other special characters are not supported.': 'varchar(500)',

'Indicates the form factor / type of speaker': 'varchar',

'Select one of the following options: \ncentimeter_kilograms\nfoot_pounds\ninch_ounces\ninch_pounds\nkilonewtons\nnewton_meters\nnewton_millimeters\nnewtons': 'varchar',

'An alphanumeric string; 250 characters maximum length per bullet point. Please do not include an actual bullet point object, just the text used to describe your product. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(250)',

'Select either Months or Years': 'varchar',

'Use the column Sport in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Select a value from the Valid Values worksheet. Only these values will be accepted.': 'varchar',

'Insert the hazmat class mentioned in section 14 of  the Material Safety Data Sheet. \n2.1: compressed gas\n2.2: liquefied gas\n3: flammable liquids\n4.1: flammable solids\n5.1: oxidizer\n5.2: organic peroxide\n6.1 toxic substance\n8: corrosive substance\n9: miscellaneous dangerous substance': 'varchar',

'Select: Remote Included or leave blank': 'varchar',

    "'Use the column Material  in the Valid Values list. An alphanumeric string; 50 characters maximum." : 'varchar(50)',

'less than 500:1, 500:1 to 1200:1, exceeding 1200:1': 'varchar(50)',

'Please see list of valid values': 'varchar',

'An alphanumeric string with a maximum of 50 characters.': 'varchar(50)',

'Alphanumeric string, max 50 characters': 'varchar(50)',

'Use the column MountType in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'motorized altazimuth': 'varchar',

'Any value in the durometer hardness scale': 'varchar',

'Select one of the following options:  male\nfemale\nunisex': 'varchar',

'Length of warranty for the lamp of the projector': 'varchar',

'The number of items that are included in the product': 'varchar',

'Nickel-Cadmium, Lithium-Ion, Nickel-Metal Hydride, Alkaline, Lithium': 'varchar',

'Select one of the following options:\nPrivateLabel\nSpecialized\nNonConsumer\nPreConfigured': 'varchar',

'Please refer to the Valid values tab for the appropriate value for this field. If color has been populated, you must populate ColorMap.': 'varchar',

'A number with up to 18 digits allowed to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas or dollar signs.': 'numeric(18, 2)',

'An alphanumeric string; 1000 characters maximum length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(1000)',

'Please use the classifier tool or Browse Tree Guides (BTGs) to determine the most accurate category for your product.': 'varchar',

'Select a Value from the Valid Values worksheet.': 'varchar',

'Please select a value from the Valid Values tab. \nBaby (less than 1 year)\nYoung (1 – 3 years)\nAdult (3 – 6 years)\nMature Adult (6 years and older)': 'varchar',

'Select one of the following options:  Wedge or Platform.': 'varchar',

'bluetooth, rf, ir, wi-fi, airplay, vhf, uhf, am, fm, am/fm, shortwave, 3g, 4g, gprs, gsm': 'varchar',

'An alphanumeric string; 50 characters maximum. If multiple colors are available, a unique record should be submitted for each product.': 'varchar(50)',

'Images should have 72-pixels-per-inch resolution and be 500 pixels minimum in length (on the longest side). The preferred file format is JPEG (.jpg), and the URL must be fully-formed and valid (i.e., include http://). When naming your image, you may use the following convention (though not required): Product SKU + View Indicator (.main) + File Extension (.jpg). An example would be: "15774.main.jpg".  There cannot be any spaces or high ascii characters in the image url.  Save the image to your Web server and supply the URL to the image in this field.  Accepted formats are .jpeg, .jpg, and .gif': 'varchar',

'Please see Valid Values tab.': 'varchar',

'A number range.': 'varchar',

'Text. HTML tags and special characters not on a standard keyboard (eg. ®, ©, ™ or other Type 1 High ASCII characters) are not supported': 'varchar',

'A valid URL, including leading "https://"\n\nThe url is case sensitive, so make sure to use matching capitalization and no redirections (e.g. .jpeg instead of .jpg). While a web browser might be smart enough to locate your image despite of these little inaccuracies, our image collection process isn\'t.': 'varchar',

'String (50)': 'varchar(50)',

'The type of human interface available for input.': 'varchar',

'A valid two-character country code.  Please select a value from the Valid Values tab.': 'varchar',

'The language of the closed-captioning or subtitles for the hearing impaired, if applicable.  Select from the list of valid values.': 'varchar',

'What are additional attributes of the product?': 'varchar',

'The model of the fastener': 'varchar',

'An additional text field where you can indicate any additional relevant product information.': 'varchar',

'not_water_resistant,  water_resistant,  waterproof': 'varchar',

'Select one of the following options: GR, KG, OZ, or LB. Do not include the actual weight, which will be collected in the package-weight field.': 'varchar',

'TRUE, FALSE': 'varchar',

'Select: True (if your product is subject to this rule).  If your product is not Autographed, you may leave this field blank.': 'varchar',

'A whole or fractional number; assumed to be in seconds (s)': 'varchar',

'Any number between 15.5 and 22, to the second decimal place.': 'numeric(2, 2)',

'The price at which the product is sold at in the local currency. Please do not use commas or currency symbols.': 'numeric',

'Select: true (if your product is subject to this rule).  If your product is not Autographed, you may leave this field blank.': 'varchar',

'Select one of the following options: \nSize\nSize, Frame Material\n': 'varchar',

'Select appropriate values from the drop-down provided or from the Valid Values tab.': 'varchar',

'select values from': 'varchar',

'Select from the following valid values:\nEnglish': 'varchar',

'A text string; 2000 characters maximum in length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(2000)',

'Text; 1,00 characters maximum length': 'varchar(1000)',

'Entering 1 will enable Make an Offer while 0 will disable Make an Offer for this listing': 'int',

    "Manufacturer's suggested retail price. This is not the price that Amazon customers will pay for your product." : 'numeric',

    "This is a free text field and should contain information if 'software-platform-grouping' is set to 'true' and a value is entered for 'computer-hardware-platform'.  Using correct syntax, enter up to 500 characters containing all system requirements." : 'varchar(500)', 

'Dedicated\nNon-dedicated' : 'varchar',

'not currently used for CE': 'varchar',

'Select one of the following options: true or false (Default is "false" if you enter no data)': 'varchar',

'A number with up to 4 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas.': 'numeric(4, 2)',

'A number with up to 12 digits allowed to the left of the decimal point and 4 digits required to the right of the decimal point. Please do not use commas.': 'numeric(12, 4)',

'flash-tubes, external-batteries, battery-packs-general, shoulder-battery-packs, belt-battery-packs, adapters-general, ac-adapters, dc-adapters, battery-chargers, ac-power-supply, dc-power-supply, other-power-supplies': 'varchar',

'See Valid Values': 'varchar',

'Describe the detail associated with the parts warranty if you have selected parts in manufacturer warranty type': 'varchar',

'A positive whole number. The unit "TPI", Teeth Per Inch, will be appended to the value automatically, so that a value of 14 will display as 14 TPI.': 'int',

'String, max 200 characters': 'varchar(200)',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas.': 'numeric(10, 2)',

'A positive whole number. W for watts will be appended to the value, so that a value of 60 will display as 60 W.': 'int',

'Positive integer, max 3 digits, no decimal point': 'int',

    "Select 'true' if your product is subject to this rule" : 'varchar', 

    'A positive whole number.': 'int',

'Percentage number': 'int',

'Number of collectibles produced': 'int',

'Number; assumed to be in frames per second': 'int',

'Select the appropriate value from the drop-down provided.  Only films rated by the MPAA in their current version may list an MPAA rating.': 'varchar',

'Identifies the entity that authenticated the collectible/item.': 'varchar',

'PrivateLabel\nSpecialized\nNonConsumer\nPreConfigured.': 'varchar',

'Canon EF, Canon EF-S, Nikon F, Nikon F(DX), Nikon (DX), Nikon (FX), Olympus/Panasonic Standard 4/3, Olympus/Panasonic Micro 4/3, Pentax KAF, Pentax KAF2, Pentax KAF3, Sony Alpha, Sigma SA, Leica M, Samsung NX': 'varchar',

'Select one of the following options: MM, CM, M, IN, or FT.': 'varchar',

'An alphanumeric string up to 50 characters.': 'varchar(50)',

'An alphanumeric string; 1 character minimum in length and x characters maximum in length.': 'varchar',

'Accepted units of measure are MM, CM, M, IN, FT.': 'varchar',

'Select "Turn Signal Indicator" if the side mirror comes with a turn signal indicator, else leave this column blank.': 'varchar',

'GR, KG, OZ, or LB. Do not include the actual weight, which will be collected in the shipping-weight field.': 'varchar',

'Positive integer, up to 10 digits, no digits after the decimal point': 'int',

    "Unique Identifier. If you don't enter a SKU we'll create one for you." : 'varchar',

 'Select one of the following options: MM, IN, CM, FT, M': 'varchar',

'Text - HTML tags and special characters not on a standard keyboard (eg. ®, ©, ™ or other Type 1 High ASCII characters) are not supported': 'varchar',

'The style of the item': 'varchar',

'An alphanumeric string. If multiple sizes are available, a unique child record should be submitted for each product.': 'varchar',

'Please refer to the Valid values tab for the appropriate value for this field.': 'varchar',

'A whole number between 1 and 11': 'int',

'Select one of the following options: \nGR\nKG\nOZ\nLB\nNote:  Do not include the actual weight, which will be collected in the shipping-weight field.': 'varchar',

'focus-free\nmanual\nmanual-and-auto': 'varchar',

'Use the column MaterialType in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'linux\nmac\nwindows\nunix': 'varchar',

'Valid values for stonecreationmethod:\nnatural\nsynthetic\nsimulated': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas.The unit of measure is always hours': 'numeric(10, 2)',

'A number with up to 12 digits allowed to the left of the decimal point and 4 digits allowed to the right of the decimal point. Please do not use commas.': 'numeric(12, 2)',

'Select one of the following options: GR, KG, OZ, or LB. Do not include the actual weight, which will be collected in the ShippingWeight field.': 'varchar',

'A number with up to 10 digits to the left of the decimal point and up to 2 digits to the right of the decimal point. Please do not use commas.': 'numeric(10, 2)',

'Use the column BottomStyle in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Number; up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point.': 'numeric(10, 2)',

'Positive integer, max 4 digits, minimum 2 digits, no decimal point': 'int',

'An alphanumeric string; 1 character minimum in length and 1500 characters maximum in length.\nThis is an additional free text field to indicate any additional relevant product information. There is also a capability within this field to add name:value pairs to the technical specs on the website for your item. If you wish to utilize this functionality, you need to submit your text entry in this field with the following format: \nnv: name1^value1 | name2^value2 | name3^value3 | nameX^valueX\nBy leading your entry with "nv" you tell us to parse the field as additional tech spec line entries for the site. You name and value need to be separated by a carrot ^ and each name value pair need to be separated by a space pipe space.': 'varchar(1500)',

'Please refer to the Sporting Goods Style Guide . An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'buttons, keypad, touch_screen, dial, keypad_pinyin, touch_screen_stylus_pen, handwriting_recognition, keypad_stroke, trackpoint_pointing_device, keyboard, microphone': 'varchar',

'A number with up to 2 decimal places. Please use a full stop (.) rather than a comma (,) for a decimal point': 'numeric',

'Images should have 72-pixels-per-inch resolution and be 500 pixels minimum in length (on the longest side). The preferred file format is JPEG (.jpg). When naming your image, you may use the following convention (though not required): Product SKU + View Indicator (i.e., .main) + File Extension (i.e., .jpg). An example would be: "15774.main.jpg". Save the image to your Web server and supply the URL to the image in this field.   BE SURE TO MAKE THE URL A FULL-PATH URL (i.e. include http://).': 'varchar',

'The price at which the product is placed on sale at in the local currency. Please do not use commas or currency symbols.': 'numeric',

'In-Ear,On-Ear,Over-Ear': 'varchar',

'Text; 500 characters maximum length per bullet point. Please do not include an actual bullet point object, just the text used to describe your product. Note: ASCII characters (®, ©, ™, etc.) and other special characters are not supported.': 'varchar(500)',

'See list of values in the Valid Values section': 'varchar',

'Select one of the following options: GR, KG, OZ, or LB. Do not include the actual weight, which will be collected in the shipping-weight field.': 'varchar',

'surface, flush, optional, wearable': 'varchar',

'An alphanumeric string; 1 character minimum in length and 1,00 characters maximum in length.': 'varchar',

'For whom is the product intended?': 'varchar',

'A positive whole number - please do not use fractions/decimals. The unit "kelvin" will be appended to the value automatically, so that a value of 2700 will display as 2700 ke.': 'int',

'This is a string of text with a maximum of 50 characters.': 'varchar',

'Select: true or false': 'varchar',

'Select a subject content value from the BTG': 'varchar',

'The ship configuration group for an offer. The ship configuration group is created and managed by the seller through the ship setting UI.': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point.  The unit "HP" will be appended to the value automatically, so that a value of 10 will display as 10 HP.': 'numeric(10, 2)',

'Identify a product related to your listing by providing the correct ASIN, UPC, EAN, GCID or GTIN for the related product. For bundles, identify one of the products contained within the bundle. For replacement parts, identify a product the part is compatible with. For parts of a set, identify the set."': 'varchar',

'String, max 100 characters': 'varchar(100)',

'An alphabetic string of up to 200 characters in length.  If there is more than one credited director, separate their names using a semicolon.  Enter no more than 5 names.': 'varchar(200)',

'Refer to the Browse Tree Guide (BTG) for valid values.  This can be found under the Inventory File Templates topic of Seller Central Help.': 'varchar',

'A numeric string stated in either months or years.': 'numeric',

'This is in addition to the valid values that you must submit for your product.': 'varchar',

'Select one of the following options: \nmonths\nyears': 'varchar',

'Select: Bit': 'varchar',

'Pick from list of valid values': 'varchar',

'IN': 'varchar',

    "An alphabetic string of up to 200 characters in length; separate different actors' names using a semicolon.  Enter up to 5 names." : 'varchar',

 'A text string; 125 minimum and 2000 maximum characthers in length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.\n\n- Keep copy informative, friendly and relevant\n- Don’t use exclamation marks or expletives\n- Refer to and expand upon your product features\n- Use <p> to add paragraphs to your text' : 'varchar(200)',

'The total product quantity in terms of the unit of measure defined in unit_count_type. Total is referring to the "total_eaches" that the customer will receive, if they place a single order, multiplied by the "each_unit_count" value. ': 'int',

'Please see the Valid Values worksheet for the list of accepted values.': 'varchar',

'Select one of the following options:  true or false.': 'varchar',

'DLP, LCD, LCoS': 'varchar',

'An alphanumeric string; 25 characters maximum.\n': 'varchar(25)',

'Glossy, Matte': 'varchar',

'Select one of the following:\nCM\nIN': 'varchar',

'For most products, this will be identical to the model number; however, some manufacturers distinguish part number from model number.': 'varchar',

'Please select a value from the Valid Values tab.': 'varchar',

'35mm, large-format, medium-format, normal, telephoto, wide-angle, zoom, other-projector-lenses': 'varchar',

'Used; Like New\nUsed; Very Good\nUsed; Good\nUsed; Acceptable\nCollectible; Like New\nCollectible; Very Good\nCollectible; Good\nCollectible; Acceptable\nNew': 'varchar',

'The maximum quantity of the product that a customer may purchase in one order': 'int',

'This is a string of text with a maximum of 40 characters.': 'varchar(40)',

'To select a proper shipping name, refer to the hazardous materials table at 49 CFR 172.101, and look for a descriptive name that corresponds to the hazards of your material.': 'varchar',

'Price based on condition': 'varchar',

'A description of whether the speaker is wired, wireless-ready, or wireless': 'varchar',

'refer to the BTG for Entertainment Collectibles for correct values': 'varchar',

'Select from the following valid values: \nLB\nOZ\nGR\nKG': 'varchar',

'CCD, CMOS, Super CCD': 'varchar',

'Any valid GCID, UPC, ISBN, or EAN.': 'varchar',

'Ethernet, Wireless, Powerline': 'varchar',

'String, max 50 characters': 'varchar(50)',

'Select one of the following options: normal, oily, dry': 'varchar',

'1x, 2x, 4x, 6x, 8x, 10x, 12x, 14x, 16x, 18x, 20x, 22x, 24x, 26x, 28x, 30x, 32x, 34x, 36x, 38x, 40x': 'varchar',

'An alphanumeric string; 40 characters maximum.': 'varchar(40)',

'Type of power source for the item.': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits required to the right of the decimal point. Please do not use commas, and make sure to include 2 digits to the right of the decimal point.': 'numeric(10, 2)',

'Text; 50 characters maximum length': 'varchar(50)',

'An alpha string up to 50 characters per box.': 'varchar(50)',

'IN, FT, MM, CM, M': 'varchar',

'full-size, compact, ultra-compact': 'varchar',

'Select a value from the Valid Values sheet.': 'varchar',

'Images should have 72-pixels-per-inch resolution and be 500 pixels minimum in length (on the longest side). The preferred file format is JPEG (.jpg), and the URL must be fully-formed and valid (i.e., include http://). When naming your image, you may use the following convention (though not required): Product SKU + View Indicator (.main) + File Extension (.jpg). An example would be: "15774.main.jpg".  There cannot be any spaces or high ASCII characters in the image url.  Save the image to your Web server and supply the URL to the image in this field.  Accepted formats are .jpeg, .jpg, and .gif.\nThe url is case sensitive, so make sure to use matching capitalization and no redirections (e.g. .jpeg instead of .jpg). While a web browser might be smart enough to locate your image despite of these little inaccuracies, our image collection process isn\'t.': 'varchar',

    "Valid values are: 'true' or 'false'. 'true' indicates online play is supported." : 'varchar',

'any valid datetime, with timezone': 'varchar',

'Any number (in Lumens)': 'numeric',

'Please select one of the following values: \n\nparent\nchild': 'varchar',

'Use Valid Values column PadType. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'An alphanumeric string; 1 character minimum in length and 80 characters maximum in length.': 'varchar(80)',

'See valid values tab for specific options.': 'varchar',

'Select from the following valid values:\nsquare-in\nsquare-ft\nsquare-cm': 'varchar',

'Select from the following valid values: \nIN\nCM': 'varchar',

'Identifies the entity that graded the collectible/item.': 'varchar',

'Select a value from the Valid Values sheet..': 'varchar',

'This is an additional free text field to indicate any additional relevant product information.': 'varchar',

'Accepted units of measure are TB, GB, MB, or KB.': 'varchar',

'iPod Built-in Dock, iPod cable included, iPod cable optional, Bluetooth Built-in, Bluetooth included, Bluetooth optional, HD Radio Built-in, HD Radio optional, Satellite Radio optional': 'varchar',

'An alphanumeric string; 1 character minimum in length and 150 characters maximum in length.': 'varchar(150)',

'A 4-digit number reflecting the year the movie or TV program was first released in theaters or shown on television.': 'int',

'Select a value or an example from the Valid Values worksheet.': 'varchar',

'A whole number': 'int',

    "An alphanumeric string detailing the size of the product that a customer would select when purchasing.  It should include the size, width, size system, gender (and appropriate age group for kids shoes).  See the Seller Central help article titled 'Shoe Size Guidelines, Charts, and FAQ' for more guidance." : 'varchar',

'A whole number between 1 and 14' : 'int',

'Select the appropriate language from the valid values provided.': 'varchar',

'An alphanumeric text string; 1 character minimum and 50 characters maximum.': 'varchar(50)',

'An numeric string, in yyyy format': 'int',

'Select from these values: cubic-cm, cubic-ft, cubic-in, cubic-m, cubic-yd, cup, gallon, liter, ounce, pint, quart': 'varchar',

'Select: MHz or GHz': 'varchar',

'Wireless standard according to the Institute of Electrical and Electronics Engineers (IEEE) if applicable (802.11g/n).': 'varchar',

'This describes the opacity of hosiery.': 'varchar',

'Select one of the following options: Update, PartialUpdate or Delete.': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits allowed to the right of the decimal point. Please do not use commas.': 'numeric(10, 2)',

'Please see valide values list': 'varchar',

'Select from the list of valid values.': 'varchar',

'A free form text string with 50 character maximum': 'varchar(50)',

'Select "variation"': 'varchar',

'Any number minumum - Any number maximum': 'numeric',

    "Select the appropriate value.  If you have Macro's turned on just select the correct value.  If you have Macro's turned off please copy and paste the correct Sport Type from the Valid Values tab." : 'varchar', 

    'If the item is a child in a parent-child relationship, enter: Variation' : 'varchar',

'Select: True or False': 'varchar',

'Hardware platform.': 'varchar',

'Select from one of the following:\n\nbatteries_only\nbatteries_contained_in_equipment\nbatteries_packed_with_equipment': 'varchar',

'A text string; 1,500 characters maximum in length.': 'varchar(1500)',

'List of valid values': 'varchar',

'A positive integer.  The unit of measure is pages-per-minute.': 'int',

'Auto-accept customer offers within the discount range.': 'varchar',

'String. 80 characters in length': 'varchar(80)',

'For speakers, the frequency response of the speaker.': 'varchar',

'Weight of the product when packaged to ship': 'int',

'A positive whole number. The unit "Lumen" will be appended to the value automatically, so that a value of 140 will display as 140 Lumen.': 'int',

'Use the column JerseyType in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Use the column BrakeType in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Please select one of the following values: parent, child': 'varchar',

'An alphanumeric string; 1 character minimum in length and 250 characters maximum in length.': 'varchar(250)',

'Use the column FitType in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Whole number': 'int',

'Use the column Material in the Valid Values list.. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Select one of the following options: Update, PartialUpdate, or Delete.': 'varchar',

'Images should have 72-pixels-per-inch resolution and be 500 pixels minimum in length (on the longest side). The preferred file format is JPEG (.jpg), and the URL must be fully-formed and valid (i.e., include http://). When naming your image, you may use the following convention (though not required): Product SKU + View Indicator (.main) + File Extension (.jpg). An example would be: "15774.main.jpg".  There cannot be any spaces or high ASCII characters in the image url.  Save the image to your Web server and supply the URL to the image in this field.  Accepted formats are .jpeg, .jpg, and .gif': 'varchar',

'Select a value from the following:\nMG\nGR\nKG\nOZ\nLB\nDWT\nCARATS': 'varchar',

'A whole number between 1 and 17': 'int',

'Select other item attribute values from the BTG': 'varchar',

'Select one of the following options: \nOZ, LB, GR, KG': 'varchar',

'backpacks, beltpacks, briefcases, holster-style-cases, portfolios, print-cases, roller-cases, vests, wraps, waist-style-cases, compact-cases, pouches': 'varchar',

'Select: monochrome or color': 'varchar',

'Select one of the following options: minutes, hours, days, weeks, months, or years.': 'varchar',

'An alphanumeric string; 100 characters maximum length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(100)',

'Select: CCD or CMOS': 'varchar',

'Supported internet applications': 'varchar',

'Text; 40 characters maximum length': 'varchar(40)',

'An alphanumeric string; 500 characters maximum length per bullet point. Please do not include an actual bullet point object, just the text used to describe your product. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar',

'Model of the fastener': 'varchar',

'A string of text no longer than 150 characters.  If you are entering multiple breeds please separate with commas.': 'varchar(150)',

    "4-digit number (e.g. '2011')" : 'int',

'Date in this format: yyyy-mm-dd': 'date',

'The main format of the film. Select from the list of valid values.': 'varchar',

'A positive integer, max 7 digits, no decimal point': 'int',

'An alphanumeric string; 1 character minimum in length and 50 characters maximum in length.\n\nFor items with apparel sizes, please use the sizes listed on the valid values tab.': 'varchar(50)',

'Entering 1 will enable Make an Offer\n\nBlank or 0 will disable Make an Offer': 'int',

'Select one of the following options: combination, normal, oily, dry': 'varchar',

'A text string; 1,500 characters maximum in length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar',

'A whole positive number': 'int',

'GPS enabled, location capture, geotagging, matching GPS stamps to geotags': 'varchar',

'Alphanumeric string, max 20 characters,': 'varchar(20)',

'Number; assumed to be in f-stops (f)': 'int',

'Select one of the following options: \nMM \nCM\nM\nIN\nFT': 'varchar',

'An alphanumeric string; 500 characters maximum length per bullet point. Please do not include an actual bullet point object, just the text used to describe your product.  Note: Type 1 High ASCII characters (®, ©, ™, etc.), HTML tags, and other special characters are not supported.': 'varchar(500)',

'Select: true or false.': 'varchar',

'Texto libre de hasta 50 caracteres': 'varchar(50)',

'Select one of the following options: CM, IN, FT, M': 'varchar',

'Select one of the following options: GCID, UPC, EAN ASIN or ISBN': 'varchar',

'An alphanumeric string; 1 character minimum in length and 500 characters maximum in length.\n\nFor Parent SKUs:\n[Brand]+[Gender/Age Group]+[Product Line]+[Material*]+[Shoe Type]\n\nFor Child SKUs: \n[Brand]+[Gender/Age Group]+[Product Line]+[Color]+[Material*]+[Shoe Type]+[Size]': 'varchar',

'Select one of the following options: \nAccessory                                                                      Variation': 'varchar',

'Select: true (if your product is subject to this rule)': 'varchar',

'A text string; 500 characters maximum in length.': 'varchar(500)',

'An alphanumeric string; 500 characters maximum length per bullet point. Please do not include an actual bullet point object, just the text used to describe your product.  Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar',

'Plasma, LCD, TFT LCD, OLED, AMOLED, VFD, Passive matrix, Organic EL, CRT, LED-backlit, LED-sidelit, LED full-array': 'varchar',

'Select an item type value from the Browse Tree Guide.': 'varchar',

'Select: megapixels': 'varchar',

'Select one of the following options: drivers_side, passengers_side.': 'varchar',

'Number; assumed to be in millimeters (mm)': 'int',

'Use Valid Values column FillMaterialType. An alphanumeric string; 50 characters maximum.': 'varchar',

'An alphanumeric string up to 500 characters per bullet point.': 'varchar(500)',

'GPS Enabled, Location Capture, Geotagging, Matching GPS Stamps to Geotags': 'varchar',

'Select from list of valid value': 'varchar',

'Enumerated': 'int',

'An alphanumeric string; 1 character minimum in length and 40 characters maximum in length.': 'varchar(40)',

    "Select the appropriate value.  If you have Macro's turned on just select the correct value.  If you have Macro's turned off please copy and paste the correct Lot Type from the Valid Values tab." : 'varchar', 

'An alphanumeric string. If multiple sizes are available, a unique child record should be submitted for each size.': 'varchar',

'An alphanumeric string; 1 character minimum in length and 1500 character maximum in length.': 'varchar(1500)',

'The shape of the speaker - typically in-wall or in-ceiling': 'varchar',

'Select one of the following options: \nIN, FT, MM, CM, M': 'varchar',

'string, max 50 characters': 'varchar(50)',

'Provide a value that describes the actual color of the lens of the eyewear.': 'varchar',

'Please refer to the Valid Values worksheet.': 'varchar',

'Whole number; assumed to be in "times" (x).': 'int',

'Search keywords used for search indexing. Enter terms that define specific features of the product (e.g., IRDA, Bluetooth, camera) that customers may use to search.': 'varchar',

'Positive decimal, up to 3 digits before and 2 after the decimal point. Unit is inches': 'numeric(3, 2)',

'format year: yyyy': 'int',

'Select from list of valid values': 'varchar',

'A text string; 1000 characters maximum in length.': 'varchar(1000)',

'See Valid Values.': 'varchar',

'The description you provide should pertain to the product in general, not your particular item. There is a 2,000 character maximum.': 'varchar(2000)',

'A positive whole number. V for volts will be appended to the value, so that a value of 120 will display as 120 V.': 'int',

'English or Metric': 'varchar',

'Inkjet, laser, snapshot, solid ink, dot matrix': 'varchar',

'An numeric string in YYYY format': 'int',

'Select from the following valid values:\nGR\nKG\nOZ\nLB': 'varchar',

'Please choose from the following choices:\nblack\nblue\nbronze\nbrown\ngold\ngray\ngreen\nmetallic\noff-white\norange\npink\npurple\nred\nsilver\nwhite\nyellow': 'varchar',

'String, max 10 characters': 'varchar(10)',

'Please refer to the Valid Values list.': 'varchar',

'A number of days': 'int',

'A price in USD': 'numeric',

'inches, centimeters, millimeters, meters, nanometers, micrometers': 'varchar',

'Select one of the following options: \nmale\nfemale\nunisex': 'varchar',

'VERDADERO, FALSO': 'varchar',

'Accepted units of measure are Mbps, Gbps, GHz, MHz, KHz.': 'varchar',

'A number with up to 5 digits to the left of the decimal point and 1 digit to the right of the decimal point. Please do not use commas. The unit "Watts" will be appended to the value automatically, so that a value of 60 will display as 60 W.': 'numeric(5, 1)',

'An alphanumeric string; 1 character minimum in length and 100 characters maximum in length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar',

'Select a value from the following:\nMM\nCM\nM\nIN\nFT': 'varchar',

'This is in addition to the valid values that you must submit for your product.  It is in your best interest to fill in all search terms. See the BTG for Details.': 'varchar',

'The name of how the unit of a product is measured: volume, length, count.': 'varchar',

'An alphanumeric string; 1 character minimum in length and 30 characters maximum in length.': 'varchar(30)',

'A number with up to 12 digits allowed to the left of the decimal point and 2 digits allowed to the right of the decimal point. Please do not use commas.': 'numeric(12, 2)',

'Select the most appropriate value from the drop-down provided, or from the Valid Values tab.': 'varchar',

'Images should have 72-pixels-per-inch resolution and be 500 pixels minimum in length (on the longest side). The preferred file format is JPEG (.jpg), and the URL must be fully-formed and valid (i.e., include https://). When naming your image, you may use the following convention (though not required): Product SKU + View Indicator (.main) + File Extension (.jpg). An example would be: "15774.main.jpg".  There cannot be any spaces or high ASCII characters in the image url.  Save the image to your Web server and supply the URL to the image in this field.  Accepted formats are .jpeg, .jpg, and .gif': 'varchar',

'See SW or VG genre terminology in the BTG for valid values': 'varchar',

'labor+parts, labor, parts': 'varchar',

'Full-DIN, Double-DIN, Half-DIN, 1.5 DIN': 'varchar',

'A positive whole number': 'int',

'A whole number. Percentage will be automatically added.': 'int',

'Please see Valid Values tab': 'varchar',

'Use Valid Values column FuelType.  An alphanumeric string; 50 characters maximum.': 'varchar',

'manual, automatic, program, manual-and-automatic, aperture-priority, shutter-speed-priority': 'varchar',

'The material which the enclosure is made of': 'varchar',

'A place to indicate the type or types of vehicles with which the product is compatible.': 'varchar',

'Use the column PocketDescription in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Select one of the following options: True or False IF YOU CHOOSE TO USE THIS FUNCTIONALITY BY SETTING THE VALUE OF THIS FIELD TO "TRUE," YOU ARE AGREEING (A) TO USE THE CONTENT OF THE RESULTING PROP. 65 WARNING MESSAGE "AS IS" AND (B) THAT AMAZON IS NOT LIABLE TO YOU IN ANY WAY IN THE EVENT THAT THIS WARNING MESSAGE DOES NOT PROVIDE THE PARTICULAR WARNING REQUIRED BY LAW FOR YOUR PRODUCT.': 'varchar',

'Select one of the following: \nbutane\nfuel_cell\ngasoline\norm_d_class_1\norm_d_class_2\norm_d_class_3\norm_d_class_4\norm_d_class_5\norm_d_class_6\norm_d_class_7\norm_d_class_8\norm_d_class_9\nsealed_lead_acid_battery': 'varchar',

'Select and applicable variation theme.': 'varchar',

'A text string; 1500 characters maximum in length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(1500)',

    "The numeric or text version of the item's size." : 'varchar', 

    'Text; 250 characters maximum length': 'varchar(250)',

'center-spot, cross-screen, diffraction, double-exposure, enhancing, fog, hot-mirror, infrared, masks, multi-image, prism, sepia, special-contrast, speed, split-field, star-filters, other': 'varchar',

'A positive integer.  Please select a value from the Valid Values tab.': 'int',

'Refer to the Browse Tree Guide (BTG) for valid values.': 'varchar',

'Watt hours of each battery (or cell) in unit': 'varchar',

'Use the column FishingLineType in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Text; 100 characters maximum length. Note: ASCII characters (®, ©, ™, etc.) and other special characters are not supported.': 'varchar',

'windows, mac, android, linux': 'varchar',

'Use the column DisplayType in the Valid Values list.. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Select from the following valid values: \nBPA Free\nPhthalate Free\nLatex Free\nLead Free': 'varchar',

'Select the appropriate language from the drop-down provided, or from the Valid Values tab.': 'varchar',

    "An alphanumeric text string; 1 character minimum and 50 characters maximum. If multiple colors are available, a unique record should be submitted for each product. Example: Cognac or Chestnut. (Note: either of those would use 'brown' as value in 'color' field.)" : 'varchar(50)',

'Use the column SuspensionType in the Valid Values list. An alphanumeric string; 50 characters maximum.' : 'varchar',

'Number': 'int',

'weatherproof, wireless': 'varchar',

'Round, Rectangular, Square, Elliptical': 'varchar',

'Select from\nLabor\nParts\nLabor+Parts': 'varchar',

'electronic viewfinder, optical viewfinder, external viewfinder, fixed LCD, flexible LCD': 'varchar',

    "Select one of the following options:  true or false.\nSelect 'true' if your product is subject to this rule." : 'varchar',

'Use the column SpecialFeatures in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar',

'Select from the following valid values: \nKG, GR, OZ, LB': 'varchar',

'The standard-product-id must have a specific number of characters according to type: GCID (16 alphanumeric characters), UPC (12 digit number), EAN (13 digit number) or GTIN(14 digit number). Please ensure that leading zeros do not get lost when the file is exported from excel to text. This can be accomplished by formatting the numbers in these cells as text, and double checking your .txt file to ensure that no errors have occurred while exporting your file.': 'varchar',

'Max. 250 characters': 'varchar(250)',

'Any valid GCID, UPC, or EAN.': 'varchar',

'An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Male, Female': 'varchar',

'1080p, 1080i, 720p, 480p': 'varchar',

'Please see the Shoes BTG for Shoes, Handbag, Eyewear, and Shoe Accessory values.': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas.  The unit "CFM" (cubic feet per minute) will be appended to the value automatically, so that a value of 1000 will display as 1000 CFM.': 'numeric(10, 2)',

'An alphanumeric string; 1 character minimum in length and 50 characters maximum in length.\n\nThe proper format for the title is Year + Signed + Game Used + Brand + Team Name + Player Name + Sport+ Item for Sale + Authenticated\n\nNote: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(50)',

'An alphanumeric string.': 'varchar',

'Please select one of the valid value from the dropdown.': 'varchar',

'"Y" = 3 to 5 business days transit time\n"N" = 4 to 14 days transit time': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas. The unit of measure is always hours': 'numeric(10, 2)',

'Select one of the following options: CM or IN.': 'varchar',

'Working Load Limit': 'varchar',

'Text; assumed to be a number range': 'varchar',

'Select from the following Valid Values: \n\nchoking_hazard_balloon\nchoking_hazard_contains_a_marble\nchoking_hazard_contains_small_ball\nchoking_hazard_is_a_marble\nchoking_hazard_is_a_small_ball\nchoking_hazard_small_parts\nno_warning_applicable': 'varchar',

'The number of units in an each; where an each is the smallest component of a product with a UPC and the unit is how the each is measured.': 'int',

'The wireless signal type used by the product': 'varchar',

'Enumerated, select from valid values list': 'varchar',

'Number; assumed to be in degrees': 'int',

'Free text with up to 500 characters.': 'varchar(500)',

'Number; assumed to be in centimeters (cm)': 'int',

'PrivateLabel\nSpecialized\nNonConsumer\nPreConfigured': 'varchar',

'Select one of the following options: \nAccessory': 'varchar',

'Any whole number that is equal to or greater than zero.': 'int',

'auto\nfill\nflash override\nforced\nhigh speed sync\nred eye reduction\nslow shutter': 'varchar',

'The intended lighting source of the film, if any. Select from the list of valid values.': 'varchar',

'An alphanumeric string; 40 characters maximum in length.': 'varchar(40)',

'A text string': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits required to the right of the decimal point. Please do not use commas.': 'numeric(10, 2)',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point. Please do not use commas.  The unit "PSI" (pounds per sq. inch) will be appended to the value automatically, so that a value of 70 will display as 70 PSI.': 'numeric(10, 2)',

'802.11a, 802.11b, 802.11g, 802.11n': 'varchar',

'Energy Star Compliant': 'varchar',

'flash memory, hard drive': 'varchar',

'Number; assumed to be in mm': 'varchar',

'An alphanumeric string; 50 characters maximum. If multiple colors are available, a unique record should be submitted for each product.\nE.g. stainless-steel, black, ecru, cherry': 'varchar(50)',

'nickel-cadmium, lithium-ion, nickel-metal hydride, alkaline, lithium': 'varchar',

'Select from the following Valid Values:\nworld-instruments\nartist-signature-series\nleft-handed': 'varchar',

'Select One of the Valid Value                            media-format3 \nmp3 \nwav \nwma \nvqf \naiff \nmpeg \navi \ndiskette35 \ndiskette525 \ncd_rom \ndvd_rom \ncd \nusb_memory_stick': 'varchar',

'Alphanumeric string, max length 30 characters': 'varchar(30)',

'Accepted Values: \nI = high danger\nII = medium danger\nIII = minor danger': 'varchar',

'Three letter currency code': 'varchar(3)',

'The style of the item.  Please select a value from the Valid Values tab.': 'varchar',

'Text; 2,000 characters maximum length': 'varchar(2000)',

'Hr': 'varchar',

'An alphanumeric string; 50 characters maximum. Refer to the HandleMaterial column in the valid values tab.': 'varchar(50)',

'Select one of the following options: GCID, UPC, EAN (ISBN-13), ASIN or ISBN': 'varchar',

'Imported;\nMade in USA or Imported;\nMade in USA and Imported;\nMade in USA': 'varchar',

'A numeric value between 1 and 100 (inclusive).': 'int',

'A whole number between 1-16.': 'int',

'An alphanumeric string; 1 character minimum in length and 500 characters maximum in length.': 'varchar(500)',

'String - up to 200 characters': 'varchar',

'Any string up to 2000 characters.': 'varchar(2000)',

'Use the column ShoeWidth in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'An alphanumeric string; 1 character minimum in length and 500 characters maximum in length. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar',

'Select from the list of Valid Values.': 'varchar',

'A number with up to 18 digits allowed to the left of the decimal point and 2 digits allowed to the right of the decimal point. Please do not use commas or dollar signs.': 'numeric(10, 2)',

'An alphanumeric string; 1 character minimum in length and 50 characters maximum in length.\n\nFor Parent SKUs:\n[Brand]+[Gender/Age Group]+[Product Line]+[Material*]+[Shoe Type]\n\nFor Child SKUs: \n[Brand]+[Gender/Age Group]+[Product Line]+[Color]+[Material*]+[Shoe Type]+[Size]': 'varchar(50)',

'A number interval': 'int',

'Mainly Square or Rounded, or another meaningful text string': 'varchar',

'Images should have 72-pixels-per-inch resolution and be 30 pixels maximum length (on the longest side). The preferred file format is JPEG (.jpg). When naming your image, please use the following convention: Product SKU + View Indicator (i.e., .swatch) + File Extension (i.e., .jpg). An example would be: "15774.swatch.jpg". Save the image to your Web server and supply the URL to the image in this field.': 'varchar',

'Max. 100 characters': 'varchar(100)',

'An alphanumeric string up to a maximum of 40 characters in length.': 'varchar(40)',

'Please select "CustomProductBundle" to indicate if this product listing is a customized bundle or 2 or more products, or "ReplacementPart" if this product is a replacement part, or part of a set. Leave this blank for all other types of products.': 'varchar',

'any metric, preferably milliliters or millimiters': 'varchar',

'Use the multiple columns  in the Valid Values list. An alphanumeric string; 50 characters maximum.': 'varchar(50)',

'Select a value from the following:\nGR\nOZ\nDWT': 'varchar',

'Please select a value from the Valid Values.': 'varchar',

'Text - maximum 1000 characters. HTML tags and special characters not on a standard keyboard (eg. ®, ©, ™ or other Type 1 High ASCII characters) are not supported': 'varchar(1000)',

'Select from the following valid values:\nGR, KG, OZ, LB': 'varchar',

'Select one of the following options: \nGR\nKG\nOZ\nLB': 'varchar',

'Select from the following valid values: \nCM\nIN': 'varchar',

'Max. 50(?) characters.': 'varchar(50)',

'City Tour, Saltwater, Freshwater, North America, South America, Africa, Western Europe, Eastern Europe, Asia': 'varchar',

'A positive integer': 'int',

'Select one of the following options:\n\nPackage': 'varchar',

'Please refer to the BTG': 'varchar',

'A free text string. 50 character limit on a single keyword. You may enter up to 5 keywords for each product.': 'varchar(50)',

'A date in this format: yyyy-mm-dd.': 'date',

'Select from the following valid values: \nMM, CM, M, IN, FT': 'varchar',

'Select from the following valid values:\ndegrees-celsius\ndegrees-fahrenheit': 'varchar',

'Accepted unit of measure is: MB, GB, TB, KB, MO, GO, TO, KO': 'varchar',

'An alphanumeric string up to 500 characters.': 'varchar(500)',

'Accepted units of measure is: GB': 'varchar',

'Select a target audience value from the Valid Values sheet.': 'varchar',

'Select: True (if your product is subject to this rule).': 'varchar',

    "Please refer to the Valid Values worksheet.  Only use this when PowerSource is 'battery'" : 'varchar',

'Please select \"CustomProductBundl\" to indicate if this product listing is a customized bundle or 2 or more products, or \"ReplacementPart\" if this product is a replacement part, or part of a set. Leave this blank for all other types of products.': 'varchar',

'A free text string of less than 50 characters.': 'varchar(49)',

'A number with up to 10 digits to the left of the decimal point and 1 digit to the right of the decimal point. Please do not use commas.': 'numeric(10, 1)',

'Make an Offer is a feature that facilitates negotiations between Buyers and Sellers. Enable Make an Offer for a given SKU by entering true.': 'varchar',

'handle-mount, macro, ring-light, shoe-mount, other': 'varchar',

'The price at which the product is offered for sale, in the local currency.': 'varchar',

'Built-in media for TVs/Projectors (e.g. TV/DVD combo)': 'varchar',

'Select from these values:  cup, gallon, liter, ounce, pint, quart': 'varchar',

'A number with up to 10 digits to the left of the decimal point and 2 digits to the right of the decimal point.  Please do not use commas': 'numeric(10, 2)',

'Alphanumeric string, max 10 characters,': 'varchar(10)',

'average, center-weighted, multi-zone, partial, spot': 'varchar',

'Ethernet, Wireless, Powerline, Bluetooth, USB, SCSI': 'varchar',

'True, False': 'varchar',

'Select from the following valid values: \nMM\nCM\nM\nIN\nFT': 'varchar',

'Select one of the following options: GR, KG, OZ or LB. ': 'varchar',

'Select a value from the Valid Values worksheet.  Only those values will be accepted.': 'varchar',

'Select: kbps, mbps': 'varchar',

'positive integer': 'int',

'A values like embedded or protruding.': 'varchar',

'An alphanumeric string; 25 characters maximum.': 'varchar(25)',

'Unidirectional, Bidirectional': 'varchar',

'An alphanumeric string; 100 characters maximum length per bullet point. Please do not include an actual bullet point object, just the text used to describe your product. Note: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(100)',

'Grade rating values': 'varchar',

'Text; 1,000 characters maximum length': 'varchar(1000)',

'hard, soft, air, plastic, metal, cloth, aluminum, carbon-fiber, fiberglass': 'varchar',

'A number with up to 5 digits to the left of the decimal point and 1 digit to the right of the decimal point. Please do not use commas. The unit "Watts" will be appended to the value automatically, so that a value of 60 will display as 60 W. ': 'numeric(5, 1)',

'An alphanumeric string; 250 characters maximum.': 'varchar(250)',

    '4 digit': 'int',

'Enter the product tax code supplied to you by Amazon.com.': 'varchar',

'Select an item type value from the Browse Tree Guide (BTG).': 'varchar',

'An alphanumeric string; 1 character minimum in length and 500 characters maximum in length.\n\nThe proper format for the title is Year + Signed + Game Used + Brand + Team Name + Player Name + Sport+ Item for Sale + Authenticated\n\nNote: Type 1 High ASCII characters (®, ©, ™, etc.) or other special characters are not supported.': 'varchar(500)',

'Select one of the following options: \nMM\nCM\nM\nIN\nFT': 'varchar',

'Select from the dropdown list. ': 'varchar',

'Positive integer, max 5 digits, no decimal point': 'int',

    'An alphanumeric text string; 1 character minimum and 100 characters maximum.' : 'varchar(100)'
}
