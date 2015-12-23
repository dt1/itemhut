create table amazon_computers.valid_external_product_id_type (
     external_product_id_type varchar primary key
);

create table amazon_computers.valid_gtin_exemption_reason (
     gtin_exemption_reason varchar primary key
);

create table amazon_computers.valid_related_product_id_type (
     related_product_id_type varchar primary key
);

create table amazon_computers.valid_feed_product_type (
     feed_product_type varchar primary key
);

create table amazon_computers.valid_update_delete (
     update_delete varchar primary key
);

create table amazon_computers.valid_currency (
     currency varchar primary key
);

create table amazon_computers.valid_condition_type (
     condition_type varchar primary key
);

create table amazon_computers.valid_product_tax_code (
     product_tax_code varchar primary key
);

create table amazon_computers.valid_offering_can_be_gift_messaged (
     offering_can_be_gift_messaged varchar primary key
);

create table amazon_computers.valid_offering_can_be_giftwrapped (
     offering_can_be_giftwrapped varchar primary key
);

create table amazon_computers.valid_is_discontinued_by_manufacturer (
     is_discontinued_by_manufacturer varchar primary key
);

create table amazon_computers.valid_missing_keyset_reason (
     missing_keyset_reason varchar primary key
);

create table amazon_computers.valid_item_display_diameter_unit_of_measure (
     item_display_diameter_unit_of_measure varchar primary key
);

create table amazon_computers.valid_website_shipping_weight_unit_of_measure (
     website_shipping_weight_unit_of_measure varchar primary key
);

create table amazon_computers.valid_item_length_unit_of_measure (
     item_length_unit_of_measure varchar primary key
);

create table amazon_computers.valid_item_weight_unit_of_measure (
     item_weight_unit_of_measure varchar primary key
);

create table amazon_computers.valid_fulfillment_center_id (
     fulfillment_center_id varchar primary key
);

create table amazon_computers.valid_package_length_unit_of_measure (
     package_length_unit_of_measure varchar primary key
);

create table amazon_computers.valid_package_weight_unit_of_measure (
     package_weight_unit_of_measure varchar primary key
);

create table amazon_computers.valid_relationship_type (
     relationship_type varchar primary key
);

create table amazon_computers.valid_country_of_origin (
     country_of_origin varchar primary key
);

create table amazon_computers.valid_prop_65 (
     prop_65 varchar primary key
);

create table amazon_computers.valid_cpsia_cautionary_statement (
     cpsia_cautionary_statement varchar primary key
);

create table amazon_computers.valid_secure_digital_association_speed_class (
     secure_digital_association_speed_class varchar primary key
);

create table amazon_computers.valid_read_speed_unit_of_measure (
     read_speed_unit_of_measure varchar primary key
);

create table amazon_computers.valid_write_speed_unit_of_measure (
     write_speed_unit_of_measure varchar primary key
);

create table amazon_computers.valid_write_speed (
     write_speed varchar primary key
);

create table amazon_computers.valid_data_transfer_rate_units (
     data_transfer_rate_units varchar primary key
);

create table amazon_computers.valid_hard_drive_size_unit_of_measure (
     hard_drive_size_unit_of_measure varchar primary key
);

create table amazon_computers.valid_special_features (
     special_features varchar primary key
);

create table amazon_computers.valid_connector_type (
     connector_type varchar primary key
);

create table amazon_computers.valid_digital_audio_capacity (
     digital_audio_capacity varchar primary key
);

create table amazon_computers.valid_communication_interface (
     communication_interface varchar primary key
);

create table amazon_computers.valid_movement_detection_technology (
     movement_detection_technology varchar primary key
);

create table amazon_computers.valid_memory_storage_capacity_unit_of_measure (
     memory_storage_capacity_unit_of_measure varchar primary key
);

create table amazon_computers.valid_graphics_ram_size_unit_of_measure (
     graphics_ram_size_unit_of_measure varchar primary key
);

create table amazon_computers.valid_main_power_connector (
     main_power_connector varchar primary key
);

create table amazon_computers.valid_external_bay_type_units (
     external_bay_type_units varchar primary key
);

create table amazon_computers.valid_hotswap_bay_type_units (
     hotswap_bay_type_units varchar primary key
);

create table amazon_computers.valid_internal_bay_type_units (
     internal_bay_type_units varchar primary key
);

create table amazon_computers.valid_hardware_interface (
     hardware_interface varchar primary key
);

create table amazon_computers.valid_wireless_comm_standard (
     wireless_comm_standard varchar primary key
);

create table amazon_computers.valid_are_batteries_included (
     are_batteries_included varchar primary key
);

create table amazon_computers.valid_batteries_required (
     batteries_required varchar primary key
);

create table amazon_computers.valid_power_source_type (
     power_source_type varchar primary key
);

create table amazon_computers.valid_battery_type (
     battery_type varchar primary key
);

create table amazon_computers.valid_lithium_battery_packaging (
     lithium_battery_packaging varchar primary key
);

create table amazon_computers.valid_mfg_warranty_description_type (
     mfg_warranty_description_type varchar primary key
);

create table amazon_computers.valid_microphone_form_factor (
     microphone_form_factor varchar primary key
);

create table amazon_computers.valid_photo_sensor_technology (
     photo_sensor_technology varchar primary key
);

create table amazon_computers.valid_photo_sensor_resolution_unit_of_measure (
     photo_sensor_resolution_unit_of_measure varchar primary key
);

create table amazon_computers.valid_effective_video_resolution_unit_of_measure (
     effective_video_resolution_unit_of_measure varchar primary key
);

create table amazon_computers.valid_communication_standard (
     communication_standard varchar primary key
);

create table amazon_computers.valid_network_interface_description (
     network_interface_description varchar primary key
);

create table amazon_computers.valid_effective_still_resolution_unit_of_measure (
     effective_still_resolution_unit_of_measure varchar primary key
);

create table amazon_computers.valid_effective_video_comm_resolution_unit_of_measure (
     effective_video_comm_resolution_unit_of_measure varchar primary key
);

create table amazon_computers.valid_maximum_upstream_data_transfer_rate_unit_of_measure (
     maximum_upstream_data_transfer_rate_unit_of_measure varchar primary key
);

create table amazon_computers.valid_maximum_downstream_data_transfer_rate_unit_of_measure (
     maximum_downstream_data_transfer_rate_unit_of_measure varchar primary key
);

create table amazon_computers.valid_modem_type (
     modem_type varchar primary key
);

create table amazon_computers.valid_lan_port_bandwidth (
     lan_port_bandwidth varchar primary key
);

create table amazon_computers.valid_connectivity_technology (
     connectivity_technology varchar primary key
);

create table amazon_computers.valid_radio_bands_supported (
     radio_bands_supported varchar primary key
);

create table amazon_computers.valid_security_protocol (
     security_protocol varchar primary key
);

create table amazon_computers.valid_form_factor (
     form_factor varchar primary key
);

create table amazon_computers.valid_wireless_communication_technology (
     wireless_communication_technology varchar primary key
);

create table amazon_computers.valid_optical_storage_device (
     optical_storage_device varchar primary key
);

create table amazon_computers.valid_amplifier_type (
     amplifier_type varchar primary key
);

create table amazon_computers.valid_format (
     format varchar primary key
);

create table amazon_computers.valid_hand_orientation (
     hand_orientation varchar primary key
);

create table amazon_computers.valid_has_auto_focus (
     has_auto_focus varchar primary key
);

create table amazon_computers.valid_is_programmable (
     is_programmable varchar primary key
);

create table amazon_computers.valid_keyboard_description (
     keyboard_description varchar primary key
);

create table amazon_computers.valid_resolution_base (
     resolution_base varchar primary key
);

create table amazon_computers.valid_maximum_operating_distance_unit_of_measure (
     maximum_operating_distance_unit_of_measure varchar primary key
);

create table amazon_computers.valid_compatible_processor_types (
     compatible_processor_types varchar primary key
);

create table amazon_computers.valid_cooling_method (
     cooling_method varchar primary key
);

create table amazon_computers.valid_fan_size_unit_of_measure (
     fan_size_unit_of_measure varchar primary key
);

create table amazon_computers.valid_maximum_rotational_speed_unit_of_measure (
     maximum_rotational_speed_unit_of_measure varchar primary key
);

create table amazon_computers.valid_air_flow_capacity_unit_of_measure (
     air_flow_capacity_unit_of_measure varchar primary key
);

create table amazon_computers.valid_noise_level_unit_of_measure (
     noise_level_unit_of_measure varchar primary key
);

create table amazon_computers.valid_light_type (
     light_type varchar primary key
);

create table amazon_computers.valid_power_connector_type (
     power_connector_type varchar primary key
);

create table amazon_computers.valid_cooler_heatsink_material (
     cooler_heatsink_material varchar primary key
);

create table amazon_computers.valid_cooler_heatsink_compatibility (
     cooler_heatsink_compatibility varchar primary key
);

create table amazon_computers.valid_sensor_technology (
     sensor_technology varchar primary key
);

create table amazon_computers.valid_headphones_form_factor (
     headphones_form_factor varchar primary key
);

create table amazon_computers.valid_ram_memory_installed_size_unit_of_measure (
     ram_memory_installed_size_unit_of_measure varchar primary key
);

create table amazon_computers.valid_range_unit_of_measure (
     range_unit_of_measure varchar primary key
);

create table amazon_computers.valid_laser_color (
     laser_color varchar primary key
);

create table amazon_computers.valid_multi_gpu_technology (
     multi_gpu_technology varchar primary key
);

create table amazon_computers.valid_motherboard_type (
     motherboard_type varchar primary key
);

create table amazon_computers.valid_processor_socket (
     processor_socket varchar primary key
);

create table amazon_computers.valid_chipset_northbridge_description (
     chipset_northbridge_description varchar primary key
);

create table amazon_computers.valid_chipset_southbridge_description (
     chipset_southbridge_description varchar primary key
);

create table amazon_computers.valid_ram_memory_technology (
     ram_memory_technology varchar primary key
);

create table amazon_computers.valid_ram_memory_maximum_size_unit_of_measure (
     ram_memory_maximum_size_unit_of_measure varchar primary key
);

create table amazon_computers.valid_onboard_video_chipset_description (
     onboard_video_chipset_description varchar primary key
);

create table amazon_computers.valid_system_bus_standard_supported (
     system_bus_standard_supported varchar primary key
);

create table amazon_computers.valid_raid_level (
     raid_level varchar primary key
);

create table amazon_computers.valid_spdif_connector_type (
     spdif_connector_type varchar primary key
);

create table amazon_computers.valid_video_output_interface (
     video_output_interface varchar primary key
);

create table amazon_computers.valid_video_output_format (
     video_output_format varchar primary key
);

create table amazon_computers.valid_pressure_sensitivity_unit_of_measure (
     pressure_sensitivity_unit_of_measure varchar primary key
);

create table amazon_computers.valid_maximum_input_resolution_unit_of_measure (
     maximum_input_resolution_unit_of_measure varchar primary key
);

create table amazon_computers.valid_cable_length_unit_of_measure (
     cable_length_unit_of_measure varchar primary key
);

create table amazon_computers.valid_cache_memory_installed_size_unit_of_measure (
     cache_memory_installed_size_unit_of_measure varchar primary key
);

create table amazon_computers.valid_computer_cpu_manufacturer (
     computer_cpu_manufacturer varchar primary key
);

create table amazon_computers.valid_computer_cpu_speed_unit_of_measure (
     computer_cpu_speed_unit_of_measure varchar primary key
);

create table amazon_computers.valid_graphics_ram_type (
     graphics_ram_type varchar primary key
);

create table amazon_computers.valid_notebook_display_technology (
     notebook_display_technology varchar primary key
);

create table amazon_computers.valid_computer_memory_size_unit_of_measure (
     computer_memory_size_unit_of_measure varchar primary key
);

create table amazon_computers.valid_system_ram_type (
     system_ram_type varchar primary key
);

create table amazon_computers.valid_additional_drives (
     additional_drives varchar primary key
);

create table amazon_computers.valid_wireless_provider (
     wireless_provider varchar primary key
);

create table amazon_computers.valid_human_interface_input (
     human_interface_input varchar primary key
);

create table amazon_computers.valid_computer_cpu_type (
     computer_cpu_type varchar primary key
);

create table amazon_computers.valid_native_resolution (
     native_resolution varchar primary key
);

create table amazon_computers.valid_display_size_unit_of_measure (
     display_size_unit_of_measure varchar primary key
);

create table amazon_computers.valid_has_color_screen (
     has_color_screen varchar primary key
);

create table amazon_computers.valid_tuner_technology (
     tuner_technology varchar primary key
);

create table amazon_computers.valid_hardware_platform (
     hardware_platform varchar primary key
);

create table amazon_computers.valid_hard_disk_description (
     hard_disk_description varchar primary key
);

create table amazon_computers.valid_graphics_processor_manufacturer (
     graphics_processor_manufacturer varchar primary key
);

create table amazon_computers.valid_memory_clock_speed_unit_of_measure (
     memory_clock_speed_unit_of_measure varchar primary key
);

create table amazon_computers.valid_operating_system (
     operating_system varchar primary key
);

create table amazon_computers.valid_hard_disk_interface (
     hard_disk_interface varchar primary key
);

create table amazon_computers.valid_front_photo_sensor_resolution_unit_of_measure (
     front_photo_sensor_resolution_unit_of_measure varchar primary key
);

create table amazon_computers.valid_nominal_voltage_unit_of_measure (
     nominal_voltage_unit_of_measure varchar primary key
);

create table amazon_computers.valid_maximum_sample_rate_unit_of_measure (
     maximum_sample_rate_unit_of_measure varchar primary key
);

create table amazon_computers.valid_speaker_connectivity (
     speaker_connectivity varchar primary key
);

create table amazon_computers.valid_material_type (
     material_type varchar primary key
);

create table amazon_computers.valid_compatible_devices (
     compatible_devices varchar primary key
);

create table amazon_computers.valid_external_testing_certification (
     external_testing_certification varchar primary key
);

create table amazon_computers.valid_memory_bus_width_unit_of_measure (
     memory_bus_width_unit_of_measure varchar primary key
);

create table amazon_computers.valid_memory_module_type (
     memory_module_type varchar primary key
);

create table amazon_computers.valid_gpu_clock_speed_unit_of_measure (
     gpu_clock_speed_unit_of_measure varchar primary key
);

create table amazon_computers.valid_display_technology (
     display_technology varchar primary key
);

create table amazon_computers.valid_analog_video_format (
     analog_video_format varchar primary key
);

create table amazon_computers.valid_light_source_operating_life_unit_of_measure (
     light_source_operating_life_unit_of_measure varchar primary key
);

create table amazon_computers.valid_image_brightness_unit_of_measure (
     image_brightness_unit_of_measure varchar primary key
);

create table amazon_computers.valid_zoom_type (
     zoom_type varchar primary key
);

create table amazon_computers.valid_media_type_base (
     media_type_base varchar primary key
);

create table amazon_computers.valid__3d_transmission_format (
     _3d_transmission_format varchar primary key
);

create table amazon_computers.valid_remote_control_description (
     remote_control_description varchar primary key
);

create table amazon_computers.valid_trigger_voltage_unit_of_measure (
     trigger_voltage_unit_of_measure varchar primary key
);

create table amazon_computers.valid_gps_navigation (
     gps_navigation varchar primary key
);

create table amazon_computers.valid_shielding_type (
     shielding_type varchar primary key
);

create table amazon_computers.valid_power_supply_mounting_type (
     power_supply_mounting_type varchar primary key
);

create table amazon_computers.valid_power_supply_maximum_output_unit_of_measure (
     power_supply_maximum_output_unit_of_measure varchar primary key
);

create table amazon_computers.valid_supported_motherboard (
     supported_motherboard varchar primary key
);

create table amazon_computers.valid_air_duct_location (
     air_duct_location varchar primary key
);

create table amazon_computers.valid_window_location (
     window_location varchar primary key
);

create table amazon_computers.valid_buffer_size_unit_of_measure (
     buffer_size_unit_of_measure varchar primary key
);

create table amazon_computers.valid_external_hardware_interface (
     external_hardware_interface varchar primary key
);

create table amazon_computers.valid_flash_memory_type (
     flash_memory_type varchar primary key
);

create table amazon_computers.valid_data_transfer_rate_unit_of_measure (
     data_transfer_rate_unit_of_measure varchar primary key
);

create table amazon_computers.valid_power_factor_correction (
     power_factor_correction varchar primary key
);

create table amazon_computers.valid_system_bus_connector_type (
     system_bus_connector_type varchar primary key
);

create table amazon_computers.valid_power_supply_design (
     power_supply_design varchar primary key
);

create table amazon_computers.valid_efficiency (
     efficiency varchar primary key
);

create table amazon_computers.valid_cache_memory_per_processor_unit_of_measure (
     cache_memory_per_processor_unit_of_measure varchar primary key
);

create table amazon_computers.valid_included_components (
     included_components varchar primary key
);

create table amazon_computers.valid_maximum_current_unit_of_measure (
     maximum_current_unit_of_measure varchar primary key
);

create table amazon_computers.valid_connection_speed_unit_of_measure (
     connection_speed_unit_of_measure varchar primary key
);
