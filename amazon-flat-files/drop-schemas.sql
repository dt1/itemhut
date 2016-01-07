select 'begin; drop schema if exists  ' || schema_name || ' cascade; commit;'
from information_schema.schemata
where schema_name ~~* 'amazon%';

begin; drop schema if exists  amazon_home cascade; commit;
begin; drop schema if exists  amazon_sports_memorabilia cascade; commit;
begin; drop schema if exists  amazon_food_and_beverages cascade; commit;
begin; drop schema if exists  amazon_food_service_and_jan_san cascade; commit;
begin; drop schema if exists  amazon_jewelry_lite cascade; commit;
begin; drop schema if exists  amazon_food_and_beverages_lite cascade; commit;
begin; drop schema if exists  amazon_health cascade; commit;
begin; drop schema if exists  amazon_auto_accessory_lite cascade; commit;
begin; drop schema if exists  amazon_swvg cascade; commit;
begin; drop schema if exists  amazon_industrial cascade; commit;
begin; drop schema if exists  amazon_sports cascade; commit;
begin; drop schema if exists  amazon_power_transmission_lite cascade; commit;
begin; drop schema if exists  amazon_wireless cascade; commit;
begin; drop schema if exists  amazon_entertainment_collectibles cascade; commit;
begin; drop schema if exists  amazon_video cascade; commit;
begin; drop schema if exists  amazon_coins_lite cascade; commit;
begin; drop schema if exists  amazon_beauty_lite cascade; commit;
begin; drop schema if exists  amazon_pet_supplies cascade; commit;
begin; drop schema if exists  amazon_shoes cascade; commit;
begin; drop schema if exists  amazon_lab_supplies_lite cascade; commit;
begin; drop schema if exists  amazon_sports_lite cascade; commit;
begin; drop schema if exists  amazon_musical_instruments_lite cascade; commit;
begin; drop schema if exists  amazon_toys cascade; commit;
begin; drop schema if exists  amazon_watches_lite cascade; commit;
begin; drop schema if exists  amazon_baby cascade; commit;
begin; drop schema if exists  amazon_watches cascade; commit;
begin; drop schema if exists  amazon_industrial_lite cascade; commit;
begin; drop schema if exists  amazon_food_service_and_jan_san_lite cascade; commit;
begin; drop schema if exists  amazon_power_transmission cascade; commit;
begin; drop schema if exists  amazon_wireless_lite cascade; commit;
begin; drop schema if exists  amazon_clothing cascade; commit;
begin; drop schema if exists  amazon_office_lite cascade; commit;
begin; drop schema if exists  amazon_coins cascade; commit;
begin; drop schema if exists  amazon_raw_materials_lite cascade; commit;
begin; drop schema if exists  amazon_mechanical_fasteners cascade; commit;
begin; drop schema if exists  amazon_health_lite cascade; commit;
begin; drop schema if exists  amazon_pet_supplies_lite cascade; commit;
begin; drop schema if exists  amazon_consumer_electronics_lite cascade; commit;
begin; drop schema if exists  amazon_raw_materials cascade; commit;
begin; drop schema if exists  amazon_gift_cards cascade; commit;
begin; drop schema if exists  amazon_auto_accessory cascade; commit;
begin; drop schema if exists  amazon_entertainment_collectibles_lite cascade; commit;
begin; drop schema if exists  amazon_home_improvement cascade; commit;
begin; drop schema if exists  amazon_gift_cards_lite cascade; commit;
begin; drop schema if exists  amazon_baby_lite cascade; commit;
begin; drop schema if exists  amazon_sports_memorabilia_lite cascade; commit;
begin; drop schema if exists  amazon_music cascade; commit;
begin; drop schema if exists  amazon_shoes_lite cascade; commit;
begin; drop schema if exists  amazon_toys_lite cascade; commit;
begin; drop schema if exists  amazon_computers_lite cascade; commit;
begin; drop schema if exists  amazon_camera_and_photo cascade; commit;
begin; drop schema if exists  amazon_beauty cascade; commit;
begin; drop schema if exists  amazon_home_improvement_lite cascade; commit;
begin; drop schema if exists  amazon_book_loader cascade; commit;
begin; drop schema if exists  amazon_consumer_electronics cascade; commit;
begin; drop schema if exists  amazon_mechanical_fasteners_lite cascade; commit;
begin; drop schema if exists  amazon_office cascade; commit;
begin; drop schema if exists  amazon_jewelry cascade; commit;
begin; drop schema if exists  amazon_clothing_lite cascade; commit;
begin; drop schema if exists  amazon_swvg_lite cascade; commit;
begin; drop schema if exists  amazon_lab_supplies cascade; commit;
begin; drop schema if exists  amazon_home_lite cascade; commit;
begin; drop schema if exists  amazon_computers cascade; commit;
begin; drop schema if exists  amazon_musical_instruments cascade; commit;
begin; drop schema if exists  amazon_camera_and_photo_lite cascade; commit;
