from alembic import op
from sqlalchemy.orm import query, session
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer
from sqlalchemy.sql.expression import exists
from wtforms.fields.simple import StringField
from tamisemisystem import db   
from tamisemisystem.models import District, Region
from flask.helpers import flash

#from models import User
exists_regions = db.session.query(Region)
exists_districts = db.session.query(District)
if exists_regions:
    db.session.query(Region).delete()
    db.session.commit()
    regions_to_insert = [Region(regionname="Arusha"), Region(regionname="Dar es salaam"), Region(regionname="Dodoma"),
    Region(regionname="Geita"), Region(regionname="Iringa"), Region(regionname="Kagera"),
    Region(regionname="Katavi"), Region(regionname="Kigoma"), Region(regionname="Kilimanjaro"),
    Region(regionname="Lindi"), Region(regionname="Manyara"), Region(regionname="Mara"),
    Region(regionname="Mbeya"), Region(regionname="Morogoro"), Region(regionname="Mtwara"),
    Region(regionname="Mwanza"), Region(regionname="Njombe"), Region(regionname="Pemba Kaskazini"),
    Region(regionname="Pemba Kusini"), Region(regionname="Pwani"), Region(regionname="Rukwa"),
    Region(regionname="Ruvuma"), Region(regionname="Shinyanga"), Region(regionname="Simiyu"),
    Region(regionname="Singida"), Region(regionname="Tabora"),
    Region(regionname="Tanga"), Region(regionname="Unguja Kusini"), 
     Region(regionname="Unguja Kaskazini"), Region(regionname="Unguja Mjini Magharibi")]
    db.session.bulk_save_objects(regions_to_insert)
    db.session.commit()
else:
    pass
if exists_districts:
    db.session.query(District).delete()
    db.session.commit()
    districts_to_insert = [District(districtname="Arusha", region_id=1), District(districtname = "Arumeru", region_id=1),
    District(districtname="Ngorongoro", region_id=1), District(districtname = "Longido", region_id=1),
    District(districtname="Monduli", region_id=1), District(districtname = "Taratu", region_id=1),
    District(districtname="Kinondoni", region_id=2), District(districtname = "Ilala", region_id=2),
    District(districtname="Temeke", region_id=2), District(districtname = "Kigamboni", region_id=2),
    District(districtname="Ubungo", region_id=2), District(districtname="Chamwino", region_id=3), 
    District(districtname = "Dodoma Jiji", region_id=3), District(districtname="Chemba", region_id=3),
    District(districtname="Kondoa", region_id=3), District(districtname = "Bahi", region_id=3),
    District(districtname="Mpwapwa", region_id=3), District(districtname="Kongwa", region_id=3),
    District(districtname="Bukombe", region_id=4), District(districtname="Mbogwe", region_id=4),
    District(districtname="Chato", region_id=4), District(districtname="Geita", region_id=4),
    District(districtname="Mufindi", region_id=5), District(districtname="Kilolo", region_id=5),
    District(districtname="Iringa", region_id=5), District(districtname="Biharamulo", region_id=6),
    District(districtname="Karagwe", region_id=6), District(districtname="Muleba", region_id=6),
    District(districtname="Kyerwa", region_id=6), District(districtname="Bukoba Mjini", region_id=6),
    District(districtname="Ngara", region_id=6), District(districtname="Missenyi", region_id=6),
    District(districtname="Mlele", region_id=7),District(districtname="Mpanda", region_id=7),
    District(districtname="Tanganyika", region_id=7), District(districtname="Kigoma Ujiji", region_id=8),
    District(districtname="Kasulu", region_id=8), District(districtname="Kakonko", region_id=8),
    District(districtname="Uvinza", region_id=8), District(districtname="Buhigwe", region_id=8),
    District(districtname="Kibondo", region_id=8), District(districtname="Siha", region_id=9),
    District(districtname="Moshi", region_id=9), District(districtname="Mwanga", region_id=9),
    District(districtname="Rombo", region_id=9), District(districtname="Hai", region_id=9),
    District(districtname="Same", region_id=9), District(districtname="Nachingwea", region_id=10),
    District(districtname="Ruangwa", region_id=10), District(districtname="Liwale", region_id=10),
    District(districtname="Lindi", region_id=10), District(districtname="Kilwa", region_id=10),
    District(districtname="Babati", region_id=11), District(districtname="Mbulu", region_id=11),
    District(districtname="Hanang'", region_id=11), District(districtname="Kiteto", region_id=11),
    District(districtname="Simanjiro", region_id=11), District(districtname="Rorya", region_id=12),
    District(districtname="Serengeti", region_id=12), District(districtname="Bunda", region_id=12),
    District(districtname="Butiama", region_id=12), District(districtname="Tarime", region_id=12),
    District(districtname="Musoma", region_id=12), District(districtname="Chunya", region_id=13),
    District(districtname="Kyela", region_id=13), District(districtname="Mbya Mjini", region_id=13),
    District(districtname="Rungwe", region_id=13), District(districtname="Mbarali", region_id=13),
    District(districtname="Gairo", region_id=14), District(districtname="Kilombero", region_id=14),
    District(districtname="Mvomero", region_id=14), District(districtname="Morogoro", region_id=14),
    District(districtname="Ulanga", region_id=14), District(districtname="Kilosa", region_id=14),
    District(districtname="Malinyi", region_id=14), District(districtname="Newala", region_id=15),
    District(districtname="Nanyumbu", region_id=15), District(districtname="Mtwara", region_id=15),
    District(districtname="Masasi", region_id=15), District(districtname="Tandahimba", region_id=15),
    District(districtname="Ilemela", region_id=16), District(districtname="Kwimba", region_id=16),
    District(districtname="Sengerema", region_id=16), District(districtname="Nyamagana", region_id=16),
    District(districtname="Magu", region_id=16), District(districtname="Misungwi", region_id=16),
    District(districtname="Ukerewe", region_id=16), District(districtname="Njombe Mjini", region_id=17),
    District(districtname="Njombe Vijijini", region_id=17), District(districtname="Makambako", region_id=17),
    District(districtname="Wanging’ombe", region_id=17),District(districtname="Makete", region_id=17),
    District(districtname="Wete", region_id=18), District(districtname="Micheweni", region_id=18),
    District(districtname="Chake chake", region_id=19), District(districtname="Mkoani", region_id=19),
    District(districtname="Bagamoyo", region_id=20), District(districtname="Kibaha Mjini", region_id=20),
    District(districtname="Kibaha Vijijini", region_id=20), District(districtname="Kisarawe", region_id=20),
    District(districtname="Mafia", region_id=20), District(districtname="Mkuranga", region_id=20),
    District(districtname="Rufiji", region_id=20), District(districtname="Kalambo", region_id=21),
    District(districtname="Nkasi", region_id=21), District(districtname="Sumbawanga Mjini", region_id=21),
    District(districtname="Sumbawanga Vijijini", region_id=21), District(districtname="Mbinga", region_id=22), 
    District(districtname="Namtumbo", region_id=22), District(districtname="Nyasa", region_id=22),
    District(districtname="Songea Mjini", region_id=22), District(districtname="Songea Vijijini", region_id=22),
     District(districtname="Tunduru", region_id=22), District(districtname="Kahama Mjini", region_id=23),
    District(districtname="Kahama Vijijini", region_id=23),  District(districtname="Kishapu", region_id=23),
    District(districtname="Shinyanga Mjini", region_id=23), District(districtname="Shinyanga Vijijini", region_id=23),
    District(districtname="Bariadi", region_id=24), District(districtname="Busega", region_id=24),
    District(districtname="Maswa", region_id=24), 
    District(districtname="Meatu", region_id=24), District(districtname="Itilima", region_id=24),
    District(districtname="Iramba", region_id=25), District(districtname="Manyoni", region_id=25),
    District(districtname="Singida Mjini", region_id=25), District(districtname="Singida Vijijini", region_id=25),
    District(districtname="Igunga", region_id=26), District(districtname="Kaliua", region_id=26),
    District(districtname="Nzega", region_id=26), District(districtname="Sikonge", region_id=26),
    District(districtname="Uyui", region_id=26), District(districtname="Tabora Mjini", region_id=26),
    District(districtname="Urambo", region_id=26), District(districtname="Handeni", region_id=27),
    District(districtname="Kilindi", region_id=27), District(districtname="Korogwe", region_id=27),
    District(districtname="Lushoto", region_id=27), District(districtname="Mkinga", region_id=27),
    District(districtname="Muheza", region_id=27), District(districtname="Tanga Mjini", region_id=27),
    District(districtname="Kati", region_id=28), District(districtname="Kusini", region_id=28),
    District(districtname="Mjini Magharibi A", region_id=29), District(districtname="Majini Kaskazini", region_id=29),
    District(districtname="Mjini", region_id=30), District(districtname="Majini Magharibi", region_id=30)]
    db.session.bulk_save_objects(districts_to_insert)
    db.session.commit()
else:
    pass


