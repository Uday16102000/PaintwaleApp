insert into paintwale_v1.service_type(service_name, created_at) values 
('Paints',now()),
('Waterproofing',now()),
('Texture',now()),
('Stencil',now()),
('Deep Cleaning',now()),
('Wood Polish',now()),
('Touchup',now()),
('Sample',now()),
('Grouting',now()),
('Crack Filling',now()),
('Pest Control',now()),
('Staging',now()),
('Surface Preparation',now()),
('As applicable',now()),
('Projects',now()),
('Wallpaper',now()),
('Wall Panelling',now()),
('Wood Coating',now()),
('False Ceiling',now()),
('Electrical',now());


insert into paintwale_v1.product_brand(brand_name, created_at)
values 
('Asian Paints',now()),
('Nerolac Paints',now()),
('Berger Paints',now()),
('Dulux Paints',now()),
('Nippon Paints',now()),
('Dr Fixit',now()),
('Fosroc',now()),
('Birla White	Jotun',now()),
('Appolo Paints',now()),
('Indigo Paints',now()),
('JSW paints',now()),
('Perma',now()),
('Shalimar paints',now()),
('Everest	ICA	Prakritik Paints',now()),
('Sirca',now());

INSERT INTO paintwale_v1.process
(name, description,servicetype_id,created_at,active)
VALUES
( '1P', '1 coat of paint', 1,now(),1),
( '2P', '2 coats of paint', 1,now(),1),
( '1Pr + 2P', '1 coat of primer and 2 coats of paint',1,now(),1),
( '1Pu + 1Pr + 2P', '1 coat of putty,  1 coat of primer, 2 coats of paint',  1,now(),1),
( '2Pu + 1Pr + 2P', '2 coats of putty,  1 coat of primer, 2 coats of paint', 1,now(),1),
( '2APu + 1RBC + 2P', '2 coats of acrylic Putty, 1 Royale Base Coat, 2 coats of Paint',1,now(),1),
( '1P (Rental)', '1 coat of paint', 1,now(),1),
( '2P (Rental)', '2 coats of paint', 1,now(),1),
( 'Base Coat + Top Coat', 'Texture base coat and top coats', 3,now(),1),
( 'Top Coat(s)', 'Only texture top coat or top coats', 3,now(),1),
( 'As applicable', 'As per standard material application procedure', 14,now(),1),
( 'Base coat + Stencil', 'Including background and stencil', 4,now(),1),
( 'Stencil (Excl base coat)', 'Only stencil design, without background', 4,now(),1),
( '1Pr', '1 coat of Primer', 1,now(),1),
( '1Pu + 1Pr', '1 coat of Putty, 1 coat of Primer', 1,now(),1),
( '2Pu + 1Pr', '2 coats of Putty, 1 coat of Primer', 1,now(),1),
( '2APu + 1RBC', '2 coats of Acrylic Putty, 1 Royale Base Coat', 1,now(),1),
( '1 coat waterproofing', '1 coat of chemical application', 2,now(),1),
( '2 coats waterproofing', '2 coats of chemical application', 2,now(),1),
( 'Manual deep cleaning', null, 5,now(),1),
( 'Mechanized deep cleaning', null, 5,now(),1),
( 'Touchups', null, 7,now(),1),
( 'Sampling', null, 8,now(),1),
( 'Grouting', null, 9,now(),1),
( 'Crack filling', 'Filling of cracks', 10,now(),1),
( 'Pest control', 'General Pest Control', 11,now(),1),
( 'Staging', 'Scaffolding/Staging', 12,now(),1),
( '3Pu + 1Pr + 2P', '3 coats of Putty, 1 coat of Primer and 2 coats of Paint', 1,now(),1),
( '3Pu + 1Pr', '3 coats of Putty, 1 coat of Primer', 1,now(),1),
( '1Pu', '1 coat of Putty', 1,now(),1),
( '2Pu', '2 coats of Putty', 1,now(),1),
( '3Pu', '3 coats of Putty', 1,now(),1),
( '1 Coat (Surface Preparation)', null, 13,now(),1),
( '2 Coat (Surface Preparation)', null, 13,now(),1),
( '1RBC + 2P', '1 coat of Royale Base Coat, 2 coats of Paint', 1,now(),1),
( '1RBC', '1 coat of Royale Base Coat', 1,now(),1),
( '2Pu + 1Pr + Zinc + 2P', null, 1,now(),1),
( '3Pu + 1Pr + 3P', '3 coats of Putty, 1 coat of Primer and 3 coats of Paint', 1,now(),1),
( '1Pr + 3P', null, 1,now(),1),
( '1APu + 1RBC', '1 coat of Acrylic Putty, 1 Royale Base Coat', 1,now(),1),
( '1APu + 1RBC + 2P', '1 coat of acrylic Putty, 1 Royale Base Coat, 2 coats of Paint', 1,now(),1),
( '1Pr + 2P (Rental)', '1 coat of primer and 2 coats of paint', 1,now(),1),
( '2Pu + 1Pr + 1P', '2 coats of putty,  1 coat of primer, 1 coat of pai...', 1,now(),1),
( '1Pr + 2P Spray', null, 1,now(),1),
( '2pu + 1pr + 2p spray', null, 1,now(),1),
( '4Pu + 1Pr + 2P', null, 1,now(),1),
( 'POP (Punning)', null, 1,now(),1),
( 'Sanding', null, 1,now(),1),
( '2Pu + 1Pr + 3P', '2 coats of Putty, 1 coat of Primer and 3 coats of Paint', 1,now(),1),
( '2Pu + 2Pr + 2P', '2 coats of Putty, 2 coats of primer and 2 coats of Paint',  1,now(),1),
( '1Pr + 1P', null, 1,now(),1),
( '2Pr', '2 coats of primer', 1,now(),1),
( '2Pu + 2Pr', '2 coats of putty, 2 coats of primer', 1,now(),1),
( '2GreyPu+1Pr+2P', 'Grey putty + 1primer + 2paints', 1,now(),1),
( '2Pr + 2P', '2 coats of primer + 2 coats of paint', 1,now(),1),
( '1 Base + 3 Top coats', '1 base coat and 3 top coats', 2,now(),1),
( 'Scrapping', 'Scrapping', 1,now(),1),
( '1 Tile Primer + 2P', '1 coat of Tile Primer , 2 coats of Paint', 1,now(),1),
( '1Pu + 2Pr + 3P', null, 1,now(),1),
( '1APU+1RBC+3P', '1 coat of  Acrylic Putty,1 Royal Base Coat, 3 coats of paints', 1,now(),1),
( '2Apu + 1Oil Pr', '2 coats of acrylic putty, 1 coat of oil primer', 1,now(),1),
( 'Scrapping', 'To remove the paint which is peeling off', 1,now(),1),
( '4Pu+1Pr+2P', '2 coats of Birla wallcare putty,2 coats of Acrylic Putty,1 coat Primer ,2coats of Paint', 1,now(),1),
( 'Damp Sheath', '1Pr', 1,now(),1),
( 'Touchups', null, 1,now(),1),
( '1 Day Express Painting Service', 'Our superfast service which ensures your job finishes in 1 day. Conditions apply.', 16,now(),1),
( '2 Day Express Painting Service', 'Our superfast service which ensures your job finishes in 2 days. Conditions apply.', 16,now(),1),
( 'Home Protect Insurance for 2 Years', 'Get India first all-inclusive painting service which has extended warranty, discounted pricing', 16,now(),1),
( '1Pu + 2P', '1 coat putty and 2 coats of paints', 1,now(),1),
( '1 Base Coat + 2 Top Coats', '1 base coat & 2 top coat', 1,now(),1),
( '1Pu + 2Pr + 2P', '1 coat putty ,2 coat primer and 2 coats of paints',1,now(),1),
( 'Primeseal + 1WPC +1P', 'For raincoat classic and raincoat select', 1,now(),1),
( '2 Dampshield Elasto + 2p', 'Paint with waterproof base coat primer ', 1,now(),1),
( '2 Dampshield Elasto + 2P', 'Paint for every exterior paint', 1,now(),1),
( '1 Dampshield Elasto + 2P', 'Paint for every exterior paint',1,now(),1),
( 'Durocem', 'Cement coat', 14,now(),1),
( '1Wpc + 1 Top Coat', '1 coat waterproofing and 1 top coat', 2,now(),1),
( '1Pr + 1Wpc + 1 Top Coat', '1 coat primer and 1 coat waterproofing and 1 top coat', 2,now(),1),
( '2Apu + 1Oil Pr + 2P', '2 coats of acrylic putty, 1 coat of oil primer, 2 coat paint', 1,now(),1),
( 'All Protek-Shyne', '2 coats of Birla wallcare putty,2 coats of Acrylic Putty,1 coat Primer ,2coats of Paint', 1,now(),1),
( 'All Protek-Matt', '2 coats of Birla wallcare putty,2 coats of Acrylic Putty,1 coat Primer ,2coats of Paint', 1,now(),1),
( '2WPU + 1pr + 2P', '2 waterproofing putty 1 coat of primer and 2 coats of paints', 1,now(),1),
( 'Reparing', 'window reparing', 1,now(),1),
( 'wooden work', 'for modular kitchen', 1,now(),1),
( 'Scaffolding', 'Staging', 12,now(),1),
( '3P', 'TRACTOR EMULSION', 1,now(),1),
( 'WPC+Raincoat Classic', 'WPC+Raincoat Classic ', 2,now(),1),
( 'WPC+Raincoat Select', 'WPC+Raincoat Select', 2,now(),1),
( 'Primeseal + WPC + Raincoat Classic', 'Primeseal with 50% dilution and WPC + Raincoat Classic without any dilution ', 2,now(),1),
( 'Prime Seal + WPC + Raincoat Select', 'Prime Seal + WPC + Raincoat Select', 2,now(),1),
( 'Base Coat + Roof seal Classic (RTC)', 'Base Coat + Roof seal Classic (RTC)',2,now(),1),
( 'Prime Seal Plus + Roof seal Classic (RTC)', 'Prime Seal Plus + Roof seal Classic (RTC)', 2,now(),1),
( 'Prime Seal + Rain coat Select (New Coat)', 'Prime Seal + Rain coat Select (New Coat)', 2,now(),1),
( 'Prime Seal Plus + Rain coat Select (New Coat)', 'Prime Seal Plus + Rain coat Select (New Coat)', 2,now(),1),
( 'Primeseal + Roofseal Select (New Coat) + Mesh', 'Primeseal with 50% dilution+ Roofseal Select (New Coat) + Mesh without dilution ', 2,now(),1),
('Prime Seal + Roof Seal Ultra (Hydroshield PUD)', 'Prime Seal + Roof Seal Ultra (Hydroshield PUD)', 2,now(),1),
('Sureseal', 'Sureseal', 2,now(),1),
('PU injection grouting', 'PU injection grouting', 2,now(),1),
('2 Base Coat + 2 Top Coats', '1st base coat with 30% dilution and 2nd base coat without dilution. 2 top coats with 35 - 40% diluti', 1,now(),1),
('3Pu+2Pr+2P', 'Royal',1,now(),1),
('4Pu', '4 coats of putty', 1,now(),1),
('Primer + 1 coat', 'Primer one coat + one coat of waterproofing ', 2,now(),1),
('As applicable', 'As per standard material application procedure', 2,now(),1),
('Self priming + 1 Top Coat', '1st self priming coat with 10% dilution and 1 top coat without any dilution ',2,now(),1),
('Material & Installation ', 'Material & Installation ',19,now(),1),
('Grouting', 'Tile Grouting',2,now(),1),
('1Pr (Seal-O-prime)+2P', 'Repainting', 1,now(),1),
('1Pr(damp shield primer)+2P', 'Repainting', 1,now(),1),
('Primer + Membrane',null, 2,now(),1),
('Transparent Coat',null, 2,now(),1),
('Cement + Sand + URP + Water - Repair',null, 2,now(),1),
('Self Primer (2:1) + 2 coats',null, 2,now(),1),
('Cement works',null, 2,now(),1),
('Stopping the flow of water',null, 2,now(),1),
('Primer (2:1) + 1 Coat + mesh + 1 coats',null, 2,now(),1),
('Primer (2:1) + 1 Coat + mesh + 2 coats',null, 2,now(),1),
('Primer (2:1) + 2 coats',null, 2,now(),1),
('Cement + sand + Water + WP',null, 2,now(),1),
('Injecting material through Nozzle',null, 2,now(),1),
('Colouring',null, 2,now(),1),
('Filler',null, 2,now(),1),
('2 coats',null, 2,now(),1),
('Primer + 2 coats',null, 2,now(),1),
('Tile gap filling - Cement based',null, 2,now(),1),
('Tile gap filling - Epoxy based',null, 2,now(),1),
('Tile gap filling',null, 2,now(),1),
('Scaffolding',null, 2,now(),1),
('Chipping + Bond coat + Cement Mortar - Cement(1) : Sand (3) : URP (0.15)',null, 2,now(),1),
('laying of concrete (Cement : sand : water + Waterproofing chemical)',null, 2,now(),1),
('Breaking / removing the surface',null, 2,now(),1),
('Gap filing using cement and WP',null, 2,now(),1),
('Gap Filling using Epoxy Sealant',null, 2,now(),1),
('Gap Filling using PU Sealant',null, 2,now(),1),
('Primer (Primseal(2) : water(1)) + 1 Coat + mesh + 2 coats',null, 2,now(),1),
('Primer mixed with water -1 coat (2:1)',null, 2,now(),1),
('WPC + Raincoat select Top Coat - 1 coat each without dilution',null, 2,now(),1),
('Cement mortar - Cement(1) : Sand (3) : URP (0.15)  + Water - Repair',null, 2,now(),1),
('WPC - 1 coat',null, 2,now(),1),
('WPC + Raincoat Classic Top Coat - 1 coat each without dilution',null, 2,now(),1),
('Crack repair',null, 2,now(),1),
('Cleaning',null, 2,now(),1),
('Gap Filling using Silicon Sealant', null, 2,now(),1),
('Primer (Primseal(2) : water(1)) + 1 Coat + mesh +  1 coats', null, 2,now(),1),
('Self primer + 1 coat',null, 2,now(),1),
('45 GSM Mesh',null, 2,now(),1),
('Primer + Membrane ',null, 2,now(),1),
('2xPu+2P', '2X putty and paint ', 1,now(),1),
('2Pu+1Pr(dampsheath)+2P', 'Fresh painting ', 1,now(),1),
('Removal of paint', 'Scraping the paint & the putty layer until the plaster ', 2,now(),1),
('Sanding + 3P', 'Sanding of the surface and 3 coats of paint without dilution ', 1,now(),1),
('Primeseal + Self Priming + 1 Coat Raincoat Neo ', 'Primeseal+ Self priming with 10% dilution + Raincoat Neo', 2,now(),1),
('2Pu + 2Pr + 3P', '2 Coats of Putty + 2 Coats of Primer + 3 Coats of Paints', 1,now(),1),
('ManPower', 'This process is to facilitate manpower to AKP customers through PPM', 14,now(),1),
('1Pr (epoxy) + 2P for PVC moldings', 'Epoxy Moldings', 1,now(),1);

set foreign_key_checks=0;

INSERT INTO paintwale_v1.product(name, description, product_category, product_type,
 brand_id, servicetype_id,created_at) VALUES ('Tractor Emulsion', 'If you have been using distemper, it is time you shifted to Tractor Emulsion. It ensures a smooth and lively finish to the wall at almost the same cost. Tractor emulsion is formulated with smooth finish and it is available in wide range of colors and price. It comes with high durability and is available in more than 1500+ shades to give the fantastic look to the walls. Also, it provides higher coverage over distempers and may be bought at lower prices.', 'Economy', 'Interior', 1, 1, NOW()),
 ('Royale Luxury Emulsion',
 'Royale Paint is useful in an extraordinary look of your house. It resistance to dirt flow, anti-fungal, and provides Teflon surface protection. Provide a silky glowing look to interior walls with the best class finish and washability with royale paint luxury emulsion. It follows the international environmental and safety law and its standards and results in a very low degree of odour.  Its one the best class emulsion royale paint and 100% protects walls against water-based stains and increases the wall paint durability.', 'Advanced', 'Interior', 1, 1, NOW()),
 ('Royale Shyne', 'Royale Shyne Luxury Emulsion is the perfect pick if you are looking for stylish finish for your walls. The paint radiates a higher sheen and gives a smooth and luxurious finish.', 'Advanced', 'Interior', 1, 1, NOW()),
 ('Royale Aspira', 'Royale Aspira is the international gold standard in paints. It is one of the most technologically advanced paints in the world and is certified by various global benchmarking institutions. Royale Aspira imparts your walls with a soft sheen and brings out the richest of colours.', 'Advanced', 'Interior', 1, 1, NOW()),
 ('Royale Matt', 'Royale Matt is the best matt finish available in the market. When applied on walls. it provides a smooth matt finish with an elegant appeal.', 'Advanced', 'Interior', 1, 1, NOW()),
 ('Apcolite Premium Emulsion', 'The super_acrylic quality of Apcolite Premium Emulsion gives your walls a rich matte finish that radiates pure elegance and also keeps it protected from stains with its Stain Guard technology.', 'Standard', 'Interior', 1, 1, NOW()),
 ('Tractor Acrylic Distemper', 'With over 1000+ shades to choose from. Tractor Acrylic Distemper offers a wide choice in water based interior wall paints. It is acrylic distemper of the highest quality and gives the walls a delightful smooth matte finish.', 'Economy', 'Interior', 1, 1, NOW()),
 ('Ace Emulsion', 'In the case of dry to moderately humid weather. choose Ace Exterior Emulsion. It is a water based exterior wall finish that comes with silicon additives.', 'Economy', 'Exterior', 1, 1, NOW()),
 ('Apex Emulsion', 'Apex Emulsion from Asian Paints is a smooth, water-based exterior emulsion and provides excellent protection against  UV attack.', 'Standard', 'Exterior', 1, 1, NOW()),
 ('Apex Ultima', 'Asian Paint Apex Ultima is acrylic smooth emulsion paint that protects walls against algae and it contains silicon solvents for high performance. It provides excellent resistance to UV radiation and provides a long lasting brightness on walls over time. Apex Ultima paint has a property that fights against dust and keeps a wall away from dirtiness. What makes it different from other water based paint is that it is fully anti angal and top performance wall finish paint instance.', 'Advanced', 'Exterior', 1, 1, NOW()),
 ('Apex Ultima Protek', 'Apex Ultima Protek is popularly known as lamination wala paint because it has super capabilities to keep a wall away from cracks, algae, pills, and fadedness. This product is absolutely free of toxins like lead, mercury, arsenic, chromium etc and hence is environment-friendly. It better ensures the ease process of cleaning rust, dirt from walls and makes them fresh for a long time for high durability of Ultima Protek. It is also known as the best class crack filler up to 2 mm.', 'Advanced', 'Exterior', 1, 1, NOW()),
 ('Beauty Smooth Finish', 'A specially formulated emulsion paint based on a durable copolymer resin to give better beautifying and stain resistance properties.', 'Economy', 'Interior', 2, 1, NOW()),
 ('Beauty Gold', 'A specially formulated emulsion paint based on a durable copolymer resin to give better beautifying and stain resistance properties.', 'Standard', 'Interior', 2, 1, NOW()),
 ('Beauty Silver', 'A High_quality water based. matt finish paint for beautifying and protecting interior walls.', 'Standard', 'Interior', 2, 1, NOW()),
 ('Impressions Eco Clean', 'A Premium Water Based luxury emulsion with ultra rich HD finish and ease of maintenance comes with Low VOC_almost no odour.', 'Advanced', 'Interior', 2, 1, NOW()),
 ('Impressions 24 Carat', 'A water based luxury emulsion that gives your walls an exquisite look with clear HD colours and a rich smooth finish.', 'Advanced', 'Interior', 2, 1, NOW()),
 ('Impressions Metallic Finish', 'Impressions Metallic Finish from Nerolac offers smooth metallic finish and excellent washability.', 'NA', 'Interior', 2, 1, NOW()),
 ('Impressions Disney', 'Nerolacs Impressions Disney is a washable Interior Emulsion and provides high sheen to the walls.', 'NA', 'Interior', 2, 1, NOW()),
 ('Pearls Emulsion', 'A rich soft sheen finish with excellent washability and stain resistance property that enhances the visual appeal at an affordable price.', 'Advanced', 'Interior', 2, 1, NOW()),
 ('Little Master', 'Little Master is a specially developed. economical product with a smooth finish with better whiteness. opacity and coverage compared to normal distemper.', 'Economy', 'Interior', 2, 1, NOW()),
 ('Suraksha Plus', 'An acrylic exterior emulsion with unique Colour Lock+ technology. which locks in the colours ensuring they keep looking like new for long.', 'Economy', 'Exterior', 2, 1, NOW()),
 ('Suraksha Advanced', 'An acrylic exterior emulsion with unique_superior ?Anti_Algal Formula? which ensures that exteriors remain spotless for years.', 'Economy', 'Exterior', 2, 1, NOW()),
 ('Excel Total', 'A Long lasting. water based premium. high performance paint to give your walls a long lasting_all weather protection.', 'Advanced', 'Exterior', 2, 1, NOW()),
 ('Excel Tile Guard', 'A premium 100% acrylic resin_water based high performance emulsion for roof tiles_bricks.', 'NA', 'Exterior', 2, 1, NOW()),
 ('Bison Acrylic Distemper', 'Bison Acrylic Distemper is a_100% water based acrylic co_polymer emulsion designed for interior walls. Available in both factory_made ready shades and in a tintable format. it gives surfaces an elegant and durable mat finish.', 'Economy', 'Interior', 3, 1, NOW()),
 ('Bison Acrylic Emulsion', 'Berger?s Bison Acrylic Emulsion has a smooth and stylish matt finish. making it an ideal choice for the price conscious customer. It has twice the durability of distemper and is suitable for a wide variety of surfaces. Made up of special colour fast pigments with excellent anti_fading properties. it comes in a range of 10.000 shades.', 'Economy', 'Interior', 3, 1, NOW()),
 ('Rangoli Premium Emulsion', 'Bergers Rangoli Premium Emulsion gives best-in-class coverage and has enhanced bio-resistant formula.', 'Standard', 'Interior', 3, 1, NOW()),
 ('Easy Clean', 'Easy Clean gives a rich luxurious finish backed up by Cross_Linking Polymers which ensure that even stubborn stains can be cleaned easily from the wall. keeping your home looking spot_less_beautiful day after day.', 'Standard', 'Interior', 3, 1, NOW()),
 ('Silk Luxury Emulsion', 'Berger Silk epitomises luxury for your walls due to its sensual finish. supreme lustre and exotic colors. Formulated with 100% acrylic binders to enhance scratch resistance. anti_fading pigments for those rich hues and bio_resistant additives for enhanced durability. Berger Silk is the treat of a lifetime for your walls.', 'Advanced', 'Interior', 3, 1, NOW()),
 ('Walmasta', 'Walmasta is a_100% water based paint. Made of suitable pigments. it is ideal for dry climates. It has higher resistance to cracking and its matt finish makes it a less expensive alternative to cement paint.', 'Economy', 'Exterior', 3, 1, NOW()),
 ('WeatherCoat Smooth', 'WeatherCoat exterior emulsion paint made of unique pigments and additives. can withstand extreme weather conditions. Further more. it has a unique feature called ONE WAY BARRIER which enables the wall to breathe out moisture. It also comes with the highest sheen from among its compatriots with Heat Resisting technology that keeps your house upto 5 degrees cooler.', 'Standard', 'Exterior', 3, 1, NOW()),
 ('WeatherCoat All Guard', 'Silicon based paint with enhanced water resistance', 'Advanced', 'Exterior', 3, 1, NOW()),
 ('Super Smooth', 'Duluc Super Smooth is a high quality washable Emulsion and offers a rich matt silk finish.', 'Standard', 'Interior', 4, 1, NOW()),
 ('Superclean 3 in 1', 'Dulux SuperClean 3 in 1 is an interior smooth emulsion paint with tough stain repellent and anti-bacterial technology.', 'Standard', 'Interior', 4, 1, NOW()),
 ('SuperCover', 'A Premium Interior Emulsion. that delivers a a smooth matt surface.ensuring cost effectiveness and ease of application with 3 key attributes of high coverage. high opacity and matt painting film.', 'Standard', 'Interior', 4, 1, NOW()),
 ('Rainbow Colours', 'An economy range emulsion. that offers a matt finish to the walls and great value for money.', 'NA', 'Interior', 4, 1, NOW()),
 ('Velvet Touch', 'Dulux Velvet Touch is a super premium Interior Emulsion that gives ultra-smooth finish to your walls.', 'Advanced', 'Interior', 4, 1, NOW()),
 ('Promise', 'A water based exterior emulsion. ideally suited for dry or moderately humid climatic conditions.', 'Economy', 'Exterior', 4, 1, NOW()),
 ('Premium Exterior Emulsion', 'A water based 100% acrylic exterior emulsion. ideally suited for dry or moderately humid climatic conditions.', 'Standard', 'Exterior', 4, 1, NOW()),
 ('Weathershield Max', 'A technologically advanced exterior emulsion which protects exterior walls from patches of dampness in addition to algae and fungus formation caused by rain.', 'Advanced', 'Exterior', 4, 1, NOW()),
 ('Weathershield Powerflexx', 'An ultra premium. high performance exterior paint that offers protection from harshest weather conditions. Enabled to give solid protection from hairline cracks. extreme heat. rain. dirt and dust.', 'Advanced', 'Exterior', 4, 1, NOW()),
 ('Weathershield Ultra Clean', 'Dulux Weathershield Ultra Clean is a high performance exterior Emulsion designed to protect exterior surfaces from the most challenging weather conditions.', 'Standard', 'Exterior', 4, 1, NOW()),
 ('Weathershield Waterproof', 'It delivers complete waterproofing of roof and side walls. when used with Dulux Weathershield Max. by forming a thick elastic. super protective film that blocks water ingress.', 'Advanced', 'Exterior', 4, 1, NOW()),
 ('Weathershield Sunreflect', 'Dulux Weathershield Sunreflect is a white base Heat Resistant emulsion paint, suitable for exterior walls to protect them from harsh weather conditions.', 'Advanced', 'Exterior', 4, 1, NOW()),
 ('Tractor Enamel', 'Asian Paints Tractor Enamel is a solvent based finish for interiors (wood, metal and masonry surfaces) and gives an excellent long-lasting gloss.', 'Basic', 'Metal/Wood', 1, 1, NOW()),
 ('Apcolite Premium Gloss Enamel', 'Asian Paints Apcolite Premium Gloss Enamel offers a tough stain-resistant film to the surface, high shine and durability.', 'Standard', 'Metal/Wood', 1, 1, NOW()),
 ('Apcolite Premium Satin Enamel', 'Asian Paints Apcolite Premium Satin Enamel is a durable, stain-resistant paint and gives a long-lasting washable finish.', 'Standard', 'Metal/Wood', 1, 1, NOW()),
 ('Royale Luxury Enamel', 'Asian Paints Royale Luxury Enamel is water-based and gives a luxurious finish to your doors, windows, gates, grills, and interior wood.', 'Advanced', 'Metal/Wood', 1, 1, NOW()),
 ('Kool & Seal', 'Berger WeatherCoat Kool & Seal formulated with 100% Acrylic Elastomeric Polymer is a flexible waterproof coating for roof, terrace, and parapet.', 'NA', 'Exterior', 3, 1, NOW()),
 ('Nerolac Impressions Hi Gloss Enamel', 'Nerolac Impressions Hi Gloss Enamel is a stain-resistant, high gloss, smooth finish enamel and provides excellent durability.', 'Advanced', 'Metal/Wood', 2, 1, NOW()),
 ('Nerolac Synthetic Enamel Paint', 'Nerolac Synthetic Enamel is a high quality sovent based enamel formulated with opacifying pigments suitable for interior and exterior wood, metal, and walls. ', 'Standard', 'Metal/Wood', 2, 1, NOW()),
 ('Nerolac Satin Enamel', 'Nerolac Satin Enamel is formulated to provide the smoothness of Satin to masonry, wood, and metal surfaces.', 'Standard', 'Metal/Wood', 2, 1, NOW()),
 ('Dulux Satin', 'Dulux Satin, formulated with Duratough technology for interior and exterior surfaces, gives a luxurious satin-like smooth finish to the walls.', '', 'Metal/Wood', 4, 1, NOW()),
 ('Breathe Easy Enamel', 'Berger Breathe Easy Enamel is a water-based, excellent stain resistant luxury enamel for wood, metal, and masonry surfaces.', '', 'Interior', 3, 1, NOW()),
 ('Luxol Lustre', 'Berger Luxol Lustre is a sheen finish that builds a tough film on the interior walls, has excellent washable property, and gives pearl-like glow finish.', '', 'Metal/Wood', 3, 1, NOW()),
 ('Luxol Satin Enamel', 'Berger Luxol Satin Enamel is a solvent-based sheen finish for interior walls and is suitable for common areas of bathroom, kitchen, balcony, and hotel.', '', 'Metal/Wood', 3, 1, NOW()),
 ('Jadoo Enamel', 'Jadoo Enamel is a solvent-based paint especially designed for interior surfaces like doors, windows, furniture, and grills.', '', 'Metal/Wood', 3, 1, NOW()),
 ('Butterfly GP Enamel', 'Butterfly Enamel meant only for interior surfaces can be applied on wooden surfaces and select mild_steel surfaces. It is a solvent based paint which provides maximum level of gloss and complete customer satisfaction.', '', 'Metal/Wood', 3, 1, NOW()),
 ('Decoprime Cement Primer (WT)', '', '', 'Primer', 1, 1, NOW()),
 ('Exterior Wall Primer(0065)', '', '', 'Primer', 1, 13, NOW()),
 ('Asian Filling Putty', '', '', 'Putty', 1, 1, NOW()),
 ('SmartCare Damp Proof', '', 'NA', 'Waterproofing', 1, 2, NOW()),
 ('Velvet Touch Diamond Glo', 'A super premium quality. highly durable and washable emulsion paint with high sheen luxury finish. offering smooth touch of velvet and the glow of diamond.', 'Advanced', 'Interior', 4, 1, NOW()),
 ('Suraksha', 'An economical water thinnable coating. specially designed for application on exterior walls in dry or moderately humid climatic conditions.', 'Economy', 'Exterior', 2, 1, NOW()),
 ('WeatherCoat Anti Dust', 'Weathercoat Anti Dustt has a unique Dust Guard technology which doesn?t allow dust to settle on your exterior walls. It keeps your house looking new and shining for years to come.', 'Standard', 'Exterior', 3, 1, NOW()),
 ('Weathershield Protect', 'A premium exterior emulsion. providing all weather protection with high reflectivity index.', 'Standard', 'Exterior', 4, 1, NOW()),
 ('Excel', 'A Long lasting. water based premium. high performance paint to give your walls a long lasting_all weather protection.', 'Standard', 'Exterior', 2, 1, NOW()),
 ('Excel Mica Marble', 'An extremely durable UV resistant water based exterior emulsion with enhanced barrier protection. paint film re_inforcement. increased inter_coat adhesion and toughness.', 'Standard', 'Exterior', 2, 1, NOW()),
 ('Royale Atmos', 'Royale Atmos is an Eco friendly Air Purifying Paint that reduces the pollution levels in your home by neutralizing formaldehyde (a harmful pollutant). It is an air purifying paint that neutralizes formaldehyde. a harmful indoor air pollutant. and makes the indoor air healthier to breathe. Royale Atmos also emits a soothing fragrance after painting thus acting as a scented paint.', 'Advanced', 'Interior', 1, 1, NOW()),
 ('Royale Lustre', '', 'Advanced', 'Interior', 1, 1, NOW()),
 ('Silk Glamor', 'Silk Glamor Luxury Emulsion is formulated using the Crystal Reflective Technology to give an ultra_smooth finish to the walls and retain its freshness for a long time. The product is free of added APEO. formaldehyde and is low in VOC. Silk Glamor is available in metallic and non_metallic shades.', 'NA', 'Interior', 3, 1, NOW()),
 ('Velvet Touch Pearl Glo', 'A premium quality. highly durable and washable emulsion paint with best in class sheen luxury finish. with smooth touch of velvet.', 'Advanced', 'Interior', 4, 1, NOW()),
 ('Tractor Emulsion Advanced', 'Tractor Emulsion Advanced comes with Superior Anti Fungal Shield and gives a smooth finish to the wall. It is a smart choice if you have been previously using distemper.', 'Economy', 'Interior', 1, 1, NOW()),
 ('Apcolite Premium Satin Emulsion', 'Apcolite Premium Satin Emulsion offers a rich satin finish that is bound to give your walls a grand look. It is easily washable and offers excellent stain resistance.', 'Standard', 'Interior', 1, 1, NOW()),
 ('Rangoli Total Care', 'Rangoli Total Care gives the best_in_class coverage. whiteness. smoothness_finish to the walls. Its enhanced bio_resistant formula prevents the walls from fungal_algal attacks and the fine extenders helps in giving a butter_like smooth finish to the walls.', 'Standard', 'Interior', 3, 1, NOW()),
 ('Treasure Seekers - Glow', '', 'Standard', 'Interior', 1, 4, NOW()),
 ('Colorwash - Special Effects', '', '', '', 0, 3, NOW()),
 ('Fizz - Special Effects', '', '', '', 0, 3, NOW()),
 ('Spatula - Special Effects', '', '', '', 0, 3, NOW()),
 ('Bloom - Special Effects', '', '', '', 0, 3, NOW()),
 ('Trellis - Special Effects', '', '', '', 0, 3, NOW()),
 ('Cris Cross - Special Effects', '', '', '', 0, 3, NOW()),
 ('Brushing - Special Effects', '', '', '', 0, 3, NOW()),
 ('Canvas - Special Effects', '', '', '', 0, 3, NOW()),
 ('Crinkle - Special Effects', '', '', '', 0, 3, NOW()),
 ('Combing - Special Effects', '', '', '', 0, 3, NOW()),
 ('Delta - Special Effects', '', '', '', 0, 3, NOW()),
 ('Disc - Special Effects', '', '', '', 0, 3, NOW()),
 ('Dapple - Special Effects', '', '', '', 0, 3, NOW()),
 ('Sponging - Special Effects', '', '', '', 0, 3, NOW()),
 ('Ragging - Special Effects', '', '', '', 0, 3, NOW()),
 ('Seashell - Special Effects', '', '', '', 0, 3, NOW()),
 ('Spiral - Special Effects', '', '', '', 0, 3, NOW()),
 ('Splash - Special Effects', '', '', '', 0, 3, NOW()),
 ('Timber - Special Effects', '', '', '', 0, 3, NOW()),
 ('Torrent - Special Effects', '', '', '', 0, 3, NOW()),
 ('Weaving - Special Effects', '', '', '', 0, 3, NOW()),
 ('Dapple - Metallics', '', '', '', 0, 3, NOW()),
 ('Sponging - Metallics', '', '', '', 0, 3, NOW()),
 ('Colorwash - Metallics', '', '', '', 0, 3, NOW()),
 ('Fizz - Metallics', '', '', '', 0, 3, NOW()),
 ('Spatula - Metallics', '', '', '', 0, 3, NOW()),
 ('Bloom - Metallics', '', '', '', 0, 3, NOW()),
 ('Trellis - Metallics', '', '', '', 0, 3, NOW()),
 ('Cris Cross - Metallics', '', '', '', 0, 3, NOW()),
 ('Brushing - Metallics', '', '', '', 0, 3, NOW()),
 ('Canvas - Metallics', '', '', '', 0, 3, NOW()),
 ('Crinkle - Metallics', '', '', '', 0, 3, NOW()),
 ('Combing - Metallics', '', '', '', 0, 3, NOW()),
 ('Delta - Metallics', '', '', '', 0, 3, NOW()),
 ('Disc - Metallics', '', '', '', 0, 3, NOW()),
 ('Ragging - Metallics', '', '', '', 0, 3, NOW()),
 ('Seashell - Metallics', '', '', '', 0, 3, NOW()),
 ('Spiral - Metallics', '', '', '', 0, 3, NOW()),
 ('Splash - Metallics', '', '', '', 0, 3, NOW()),
 ('Timber - Metallics', '', '', '', 0, 3, NOW()),
 ('Torrent - Metallics', '', '', '', 0, 3, NOW()),
 ('Weaving - Metallics', '', '', '', 0, 3, NOW()),
 ('Marble - Royale Play Stucco', '', '', '', 0, 3, NOW()),
 ('Oak - Royale Play Infinitex', '', '', '', 0, 3, NOW()),
 ('Shale - Royale Play Infinitex', '', '', '', 0, 3, NOW()),
 ('Pebbles - Royale Play Infinitex', '', '', '', 0, 3, NOW()),
 ('Bricks - Royale Play Infinitex', '', '', '', 0, 3, NOW()),
 ('Crossroad - Royale Play Infinitex', '', '', '', 0, 3, NOW()),
 ('Ripple - Royale Play Infinitex', '', '', '', 0, 3, NOW()),
 ('Breeze - Royale Play Infinitex', '', '', '', 0, 3, NOW()),
 ('Linea - Royale Play Antico', '', '', '', 0, 3, NOW()),
 ('Classic - Royale Play Safari', '', '', '', 0, 3, NOW()),
 ('Sleet - Royale Play Safari', '', '', '', 0, 3, NOW()),
 ('Drizzle - Royale Play Dune', '', '', '', 0, 3, NOW()),
 ('Halo - Royale Play Dune', '', '', '', 0, 3, NOW()),
 ('Whirl - Royale Play Dune', '', '', '', 0, 3, NOW()),
 ('Damp Guard', '', '', 'Waterproofing', 0, 2, NOW()),
 ('Dr Fixit', '', '', '', 0, 2, NOW()),
 ('Once upon a time - Glow', '', '', '', 0, 4, NOW()),
 ('Zeroes & Ones - Glow', '', '', '', 0, 4, NOW()),
 ('Mighty Heroes - Glow', '', '', '', 0, 4, NOW()),
 ('Wild Encounters - Glow', '', '', '', 0, 4, NOW()),
 ('Travel Traiils - Glow', '', '', '', 0, 4, NOW()),
 ('Unplugged - Glow', '', '', '', 0, 4, NOW()),
 ('Howzzat - Glow', '', '', '', 0, 4, NOW()),
 ('Flying Kick - Glow', '', '', '', 0, 4, NOW()),
 ('Solar Energizer - Glow', '', '', '', 0, 4, NOW()),
 ('Rush Hour - Glow', '', '', '', 0, 4, NOW()),
 ('Queen of the Seas - Glow', '', '', '', 0, 4, NOW()),
 ('I feel like a Bird - Glow', '', '', '', 0, 4, NOW()),
 ('Bird Time Stories - Glow', '', '', '', 0, 4, NOW()),
 ('Lighthouse Island - Glow', '', '', '', 0, 4, NOW()),
 ('Slam Dunk - Glow', '', '', '', 0, 4, NOW()),
 ('Princess of Pop - Glow', '', '', '', 0, 4, NOW()),
 ('Rock On - Glow', '', '', '', 0, 4, NOW()),
 ('Desert Safari - Glow', '', '', '', 0, 4, NOW()),
 ('Rock Climber - Glow', '', '', '', 0, 4, NOW()),
 ('Jurassica - Glow', '', '', '', 0, 4, NOW()),
 ('Fun at the Circus - Glow', '', '', '', 0, 4, NOW()),
 ('Battle in the Sky - Glow', '', '', '', 0, 4, NOW()),
 ('Traffic Jam - Glow', '', '', '', 0, 4, NOW()),
 ('Choo Choo Train - Glow', '', '', '', 0, 4, NOW()),
 ('Treasure Seekers - Without Glow', '', '', '', 0, 4, NOW()),
 ('Once upon a time - Without Glow', '', '', '', 0, 4, NOW()),
 ('Zeroes & Ones - Without Glow', '', '', '', 0, 4, NOW()),
 ('Mighty Heroes - Without Glow', '', '', '', 0, 4, NOW()),
 ('Wild Encounters - Without Glow', '', '', '', 0, 4, NOW()),
 ('Travel Traiils - Without Glow', '', '', '', 0, 4, NOW()),
 ('Unplugged - Without Glow', '', '', '', 0, 4, NOW()),
 ('Howzzat - Without Glow', '', '', '', 0, 4, NOW()),
 ('Flying Kick - Without Glow', '', '', '', 0, 4, NOW()),
 ('Solar Energizer - Without Glow', '', '', '', 0, 4, NOW()),
 ('Rush Hour - Without Glow', '', '', '', 0, 4, NOW()),
 ('Queen of the Seas - Without Glow', '', '', '', 0, 4, NOW()),
 ('I feel like a Bird - Without Glow', '', '', '', 0, 4, NOW()),
 ('Bird Time Stories - Without Glow', '', '', '', 0, 4, NOW()),
 ('Lighthouse Island - Without Glow', '', '', '', 0, 4, NOW()),
 ('Slam Dunk - Without Glow', '', '', '', 0, 4, NOW()),
 ('Princess of Pop - Without Glow', '', '', '', 0, 4, NOW()),
 ('Rock On - Without Glow', '', '', '', 0, 4, NOW()),
 ('Desert Safari - Without Glow', '', '', '', 0, 4, NOW()),
 ('Rock Climber - Without Glow', '', '', '', 0, 4, NOW()),
 ('Jurassica - Without Glow', '', '', '', 0, 4, NOW()),
 ('Fun at the Circus - Without Glow', '', '', '', 0, 4, NOW()),
 ('Battle in the Sky - Without Glow', '', '', '', 0, 4, NOW()),
 ('Traffic Jam - Without Glow', '', '', '', 0, 4, NOW()),
 ('Choo Choo Train - Without Glow', '', '', '', 0, 4, NOW()),
 ('Outerspace - Ceiling - Glow', '', '', '', 0, 4, NOW()),
 ('Fairy Dust - Ceiling - Glow', '', '', '', 0, 4, NOW()),
 ('Space Zappers - Ceiling - Glow', '', '', '', 0, 4, NOW()),
 ('Magic Mermaid - Ceiling - Glow', '', '', '', 0, 4, NOW()),
 ('Outerspace - Ceiling - Without Glow', '', '', '', 0, 4, NOW()),
 ('Fairy Dust - Ceiling - Without Glow', '', '', '', 0, 4, NOW()),
 ('Space Zappers - Ceiling - Without Glow', '', '', '', 0, 4, NOW()),
 ('Magic Mermaid - Ceiling - Without Glow', '', '', '', 0, 4, NOW()),
 ('Ocean Scape - Magneto', '', '', '', 0, 4, NOW()),
 ('Jungle Tale - Magneto', '', '', '', 0, 4, NOW()),
 ('Young Scientist - Magneto', '', '', '', 0, 4, NOW()),
 ('Dancing Stars - Magneto', '', '', '', 0, 4, NOW()),
 ('Fun Fair - Magneto', '', '', '', 0, 4, NOW()),
 ('Beach Time Fun - Magneto', '', '', '', 0, 4, NOW()),
 ('Backyard Story - Magneto', '', '', '', 0, 4, NOW()),
 ('Speed Machine - Magneto', '', '', '', 0, 4, NOW()),
 ('Style Villa - Magneto', '', '', '', 0, 4, NOW());

 update product set active=1;

insert into walls(wall_name,active) values 
('Ceiling',1),
('Wall',1),
('False Ceiling',1),
('Wallpaper Wall',1),
('Door',1),
('Window',1),
('Wardrobe',1),
('Fan',1),
('Floor',1),
('Grill',1),
('Texture',1),
('Stencil',1),
('Waterproofing',1),
('Deep Cleaning',1),
('Wood Finish',1),
('Touchup',1),
('Spray Painting',1),
('Sample',1),
('Colour Change',1),
('Grouting',1),
('Crack Filling',1),
('Pest Control',1),
('Staging',1),
('Surface Preparation',1),
('Skirting',1),
('Metal',1),
('Parking Lines',1);