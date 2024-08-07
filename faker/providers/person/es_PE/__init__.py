from collections import OrderedDict
from itertools import zip_longest
from typing import Dict

from ..es import Provider as PersonProvider


class Provider(PersonProvider):
    formats_male = OrderedDict(
        [
            ("{{given_name_male}} {{last_name}} {{last_name}}", 0.55),
            ("{{first_name_male}} {{last_name}} {{last_name}}", 0.35),
            ("{{first_name_male}} {{last_name}}", 0.07),
            ("{{given_name_male}} {{last_name}}-{{last_name}} {{last_name}}", 0.01),
            ("{{first_name_male}} {{last_name}}-{{last_name}} {{last_name}}", 0.01),
            ("{{first_name_male}} {{last_name}}-{{last_name}}", 0.01),
        ]
    )

    formats_female = OrderedDict(
        [
            ("{{given_name_female}} {{last_name}} {{last_name}}", 0.55),
            ("{{first_name_female}} {{last_name}} {{last_name}}", 0.35),
            ("{{first_name_female}} {{last_name}}", 0.7),
            ("{{given_name_female}} {{last_name}}-{{last_name}} {{last_name}}", 0.01),
            ("{{first_name_female}} {{last_name}}-{{last_name}} {{last_name}}", 0.01),
            ("{{first_name_female}} {{last_name}}-{{last_name}}", 0.01),
        ]
    )

    formats = OrderedDict(
        [
            ("formats_male", 0.48),
            ("formats_female", 0.52),
        ]
    )

    # Sources for names data:
    # Servicio de Registro Civil e Identificación
    # Inquiry under Law of Transparency #AK002T0020771 for names and last names
    # https://docs.google.com/spreadsheets/d/1yJ2wVnlttoBaCMS-xWyw7fbUqe6xdYpg/edit?usp=sharing&ouid=105306283136031380407
    # Data was truncated to 500 items for each category

    # 500 male first names, weighted
    first_names_male: Dict[str, float] = OrderedDict(
        [
            ("Juan Carlos", 0.0418490110269355),
            ("Jorge Luis", 0.030461311624553355),
            ("Luis Alberto", 0.030351512869984842),
            ("Marco Antonio", 0.027198720060234337),
            ("Miguel Angel", 0.026257587878219347),
            ("José Luis", 0.025692908569010554),
            ("Carlos Alberto", 0.02327733596850522),
            ("Luis Enrique", 0.016077674776089873),
            ("Jose Luis", 0.014634605430333951),
            ("Miguel Ángel", 0.013818957539253704),
            ("Julio Cesar", 0.0136307311028511),
            ("Carlos", 0.01270528445720234),
            ("Luis Miguel", 0.01176415227518735),
            ("Julio César", 0.011528869229684097),
            ("Carlos Enrique", 0.011246529575079206),
            ("José Antonio", 0.010932818847740876),
            ("David", 0.01072890687497106),
            ("Jorge", 0.010477938293100595),
            ("Fernando", 0.00972503254748821),
            ("Luis Fernando", 0.009505435038351183),
            ("Daniel", 0.009270151992847928),
            ("Luis", 0.009254466456480715),
            ("César Augusto", 0.00901918341097746),
            ("Edwin", 0.008548617319969967),
            ("Javier", 0.008470189638134893),
            ("Manuel", 0.007717283892522509),
            ("Juan", 0.007701598356156281),
            ("Alexander", 0.00760748513795498),
            ("Cesar Augusto", 0.007513371919752693),
            ("Carlos Eduardo", 0.007121233510580273),
            ("Edgar", 0.007042805828745198),
            ("Luis Angel", 0.006917321537810457),
            ("Juan Manuel", 0.006901636001443247),
            ("José Carlos", 0.006823208319608171),
            ("Eduardo", 0.006776151710507521),
            ("Juan José", 0.006587925274104916),
            ("Ricardo", 0.006587925274104916),
            ("Walter", 0.006572239737737706),
            ("José", 0.006305585619500027),
            ("Oscar", 0.006211472401298724),
            ("Luis Antonio", 0.0061330447194646335),
            ("Diego Alonso", 0.0059605038194282586),
            ("Alfredo", 0.005913447210327607),
            ("Alejandro", 0.005913447210327607),
            ("Miguel", 0.005882076137593183),
            ("Ronald", 0.005756591846658441),
            ("Jose Antonio", 0.005756591846658441),
            ("Roberto Carlos", 0.005599736482989277),
            ("José Manuel", 0.005552679873888626),
            ("Fredy", 0.005442881119320113),
            ("Jaime", 0.005395824510219462),
            ("Mario", 0.005270340219283736),
            ("Pedro", 0.005176227001082434),
            ("Henry", 0.005160541464715223),
            ("Roberto", 0.005144855928348011),
            ("Alberto", 0.005144855928348011),
            ("Raúl", 0.005129170391981784),
            ("Luis Eduardo", 0.005113484855614572),
            ("Joel", 0.004831145201009682),
            ("William", 0.00473703198280838),
            ("Wilfredo", 0.004689975373707729),
            ("Juan Pablo", 0.004674289837340517),
            ("Roger", 0.004611547691873639),
            ("Richard", 0.004533120010038564),
            ("Julio", 0.004501748937305125),
            ("Hugo", 0.004486063400937913),
            ("César", 0.004454692328204474),
            ("Enrique", 0.0044233212554700505),
            ("Juan Diego", 0.0044076357191038225),
            ("Diego", 0.004391950182736611),
            ("Giancarlo", 0.004282151428168098),
            ("Luis Alfredo", 0.004282151428168098),
            ("Rolando", 0.004282151428168098),
            ("Victor Hugo", 0.004235094819067447),
            ("Arturo", 0.00406255391903107),
            ("Rafael", 0.004046868382663858),
            ("Wilmer", 0.00403118284629763),
            ("Francisco", 0.003999811773563207),
            ("Antonio", 0.003952755164462557),
            ("Luis Felipe", 0.0038586419462612546),
            ("Elmer", 0.0038272708735278154),
            ("José Miguel", 0.00378021426442618),
            ("Víctor Hugo", 0.00378021426442618),
            ("Rodrigo", 0.0036704155098586503),
            ("Juan Jose", 0.0035606167552901364),
            ("Guillermo", 0.0035606167552901364),
            ("Jean Carlos", 0.0035292456825557136),
            ("Juan Alberto", 0.0035292456825557136),
            ("Jorge Antonio", 0.003497874609822274),
            ("Victor Manuel", 0.003497874609822274),
            ("Orlando", 0.0034821890734550625),
            ("Abel", 0.0034508180007216233),
            ("Jose Carlos", 0.0034351324643544113),
            ("Juan Luis", 0.0034351324643544113),
            ("Juan Francisco", 0.003356704782520321),
            ("Víctor", 0.003356704782520321),
            ("Carlos Manuel", 0.0033410192461531094),
            ("Jose Manuel", 0.0033410192461531094),
            ("Samuel", 0.003325333709785898),
            ("Jean Pierre", 0.0033096481734186858),
            ("Jesús", 0.0032782771006852466),
            ("Juan Antonio", 0.0032625915643180346),
            ("Jorge Alberto", 0.0031998494188511563),
            ("Jorge Enrique", 0.0031998494188511563),
            ("Manuel Alejandro", 0.0031841638824839443),
            ("Cesar", 0.0031684783461167327),
            ("Carlos Antonio", 0.0031684783461167327),
            ("Renzo", 0.0031371072733832935),
            ("José Alberto", 0.0031057362006488703),
            ("Víctor Manuel", 0.0030900506642826423),
            ("Omar", 0.003042994055181992),
            ("Gustavo Adolfo", 0.0029645663733469173),
            ("Raul", 0.0029488808369797057),
            ("Wilber", 0.002933195300613478),
            ("Sergio", 0.002886138691512827),
            ("Francisco Javier", 0.002886138691512827),
            ("Luis Carlos", 0.0028704531551456153),
            ("Gonzalo", 0.0028547676187784033),
            ("Gustavo", 0.0028390820824111917),
            ("Jorge Eduardo", 0.0028077110096777526),
            ("Carlos Augusto", 0.0027292833278426782),
            ("Ruben", 0.0027135977914764502),
            ("Ernesto", 0.0027135977914764502),
            ("Carlos Alfredo", 0.002697912255109239),
            ("Jose", 0.0026665411823758),
            ("Andrés", 0.0026351701096413763),
            ("Victor", 0.0026194845732751488),
            ("Gabriel", 0.0026194845732751488),
            ("Kevin", 0.002603799036907937),
            ("Armando", 0.0025724279641735136),
            ("Rubén", 0.002556742427807286),
            ("Diego Armando", 0.0025410568914400744),
            ("Juan Miguel", 0.0025253713550728624),
            ("Jonathan", 0.002509685818706635),
            ("Rodolfo", 0.002509685818706635),
            ("Jhonatan", 0.0024940002823394232),
            ("Humberto", 0.002462629209605984),
            ("Jorge Armando", 0.0024312581368715605),
            ("Jean Paul", 0.0024155726005043484),
            ("Pablo", 0.0023842015277709097),
            ("Manuel Antonio", 0.0023685159914036977),
            ("Víctor Raúl", 0.0023685159914036977),
            ("Ivan", 0.0023371449186702586),
            ("Carlos Javier", 0.002274402773202396),
            ("Luis Ángel", 0.0022273461641017446),
            ("Carlos Daniel", 0.0022273461641017446),
            ("José Eduardo", 0.0021959750913683055),
            ("Renato", 0.002180289555001094),
            ("Héctor", 0.0021332329459004427),
            ("Nelson", 0.0021018618731660195),
            ("Luis Alejandro", 0.0020548052640653684),
            ("Freddy", 0.002039119727699141),
            ("Carlos Miguel", 0.002023434191331929),
            ("Luis Manuel", 0.0020077486549647176),
            ("Carlos Fernando", 0.0019920631185984896),
            ("Erick", 0.0019920631185984896),
            ("Robert", 0.0019606920458640664),
            ("Hernán", 0.0019293209731306273),
            ("Augusto", 0.0019293209731306273),
            ("Jose Miguel", 0.0019293209731306273),
            ("Dante", 0.0019136354367634155),
            ("Santiago", 0.0019136354367634155),
            ("Sebastian", 0.0019136354367634155),
            ("Moisés", 0.0019136354367634155),
            ("Manuel Jesús", 0.0018979499003962037),
            ("Leonardo", 0.0018822643640299761),
            ("Diego Fernando", 0.0018665788276627645),
            ("Moises", 0.0018508932912955527),
            ("Luis Gustavo", 0.0018508932912955527),
            ("Paul", 0.0018352077549293252),
            ("Felipe", 0.0018195222185621134),
            ("Gianfranco", 0.0017881511458276902),
            ("Mauricio", 0.0017881511458276902),
            ("Luis Guillermo", 0.0017881511458276902),
            ("Aldo", 0.0017724656094614624),
            ("Edilberto", 0.0017567800730942508),
            ("Gerardo", 0.0017567800730942508),
            ("Edison", 0.001741094536727039),
            ("Victor Raul", 0.001741094536727039),
            ("Jimmy", 0.0017254090003608117),
            ("Pedro Pablo", 0.0017254090003608117),
            ("Luis Daniel", 0.0017254090003608117),
            ("Iván", 0.0017097234639935999),
            ("Alfonso", 0.001694037927626388),
            ("Alvaro", 0.001694037927626388),
            ("Jesús Alberto", 0.0016783523912601605),
            ("Oswaldo", 0.0016783523912601605),
            ("Carlos Arturo", 0.0016783523912601605),
            ("Luis David", 0.001646981318525737),
            ("Carlos Andrés", 0.001646981318525737),
            ("Jose Alberto", 0.0016312957821585255),
            ("José Enrique", 0.0016312957821585255),
            ("Marcos", 0.0016312957821585255),
            ("Reynaldo", 0.0016156102457922977),
            ("Juan Daniel", 0.0016156102457922977),
            ("José Francisco", 0.001599924709425086),
            ("José Fernando", 0.0015842391730578745),
            ("Adolfo", 0.0015685536366916468),
            ("Diego Alejandro", 0.0015685536366916468),
            ("Martin", 0.0015528681003244352),
        ]
    )

    # 500 female first names, weighted
    first_names_female: Dict[str, float] = OrderedDict(
        [
            ("Elizabeth", 0.02482013492992498),
            ("Carmen Rosa", 0.01852174562473743),
            ("Diana Carolina", 0.017401478752274276),
            ("Milagros", 0.014015783315493122),
            ("Roxana", 0.013891309218553465),
            ("Ana María", 0.013816624760389359),
            ("Maribel", 0.013443202469567265),
            ("Karina", 0.012571883790984981),
            ("Gabriela", 0.012273145958326995),
            ("Patricia", 0.010879036072594406),
            ("Diana", 0.010729667156266193),
            ("María Elena", 0.010605193059324974),
            ("Nancy", 0.010057507032787674),
            ("Liliana", 0.009708979561354136),
            ("Edith", 0.00950982100624881),
            ("María Isabel", 0.008862555702158848),
            ("Sonia", 0.00873808160521919),
            ("Marisol", 0.008713186785830634),
            ("Sandra", 0.008688291966442078),
            ("Katherine", 0.008638502327666529),
            ("Maritza", 0.008489133411338315),
            ("Ana Maria", 0.00846423859194976),
            ("Luz Marina", 0.008439343772561203),
            ("Mariela", 0.00833976449500854),
            ("Jessica", 0.00806592148174067),
            ("María Alejandra", 0.008041026662352116),
            ("Andrea", 0.007991237023576564),
            ("Carolina", 0.007941447384799452),
            ("Vanessa", 0.00784186810724679),
            ("Gladys", 0.007816973287859796),
            ("Maria Elena", 0.007767183649082684),
            ("Claudia", 0.007418656177649146),
            ("Rosa", 0.007269287261320933),
            ("Rosmery", 0.007269287261320933),
            ("Ana Cecilia", 0.007169707983768271),
            ("Erika", 0.007169707983768271),
            ("Maria Fernanda", 0.006995444248053063),
            ("María Fernanda", 0.006970549428664507),
            ("Fiorella", 0.006895864970500401),
            ("Rosa María", 0.0068211805123362945),
            ("Silvia", 0.006796285692947739),
            ("Alicia", 0.006597127137842414),
            ("Daniela", 0.006497547860289751),
            ("Ruth", 0.006298389305185988),
            ("Maria Isabel", 0.006273494485797433),
            ("Lizbeth", 0.006273494485797433),
            ("Alexandra", 0.00617391520824477),
            ("Isabel", 0.00617391520824477),
            ("Raquel", 0.006099230750080663),
            ("Rocio", 0.005974756653141007),
            ("Miriam", 0.005974756653141007),
            ("Pamela", 0.005949861833752451),
            ("Judith", 0.005924967014363894),
            ("Vilma", 0.0059000721949769),
            ("Melissa", 0.005850282556199788),
            ("Alejandra", 0.005850282556199788),
            ("Cecilia", 0.005700913639871575),
            ("Karen", 0.005651124001096025),
            ("Lourdes", 0.005576439542931918),
            ("Yolanda", 0.005551544723543363),
            ("Beatriz", 0.005526649904154806),
            ("Norma", 0.005427070626602144),
            ("Maria Alejandra", 0.005377280987826594),
            ("Verónica", 0.005252806890885375),
            ("Ana Lucia", 0.0052279120714983805),
            ("Nelly", 0.005178122432721268),
            ("Ana Paula", 0.005153227613334275),
            ("Marleny", 0.005153227613334275),
            ("María Luisa", 0.005153227613334275),
            ("Esther", 0.005128332793945718),
            ("Magaly", 0.005053648335781612),
            ("Tania", 0.004954069058228949),
            ("Yanet", 0.004904279419453398),
            ("Mayra Alejandra", 0.004904279419453398),
            ("Paola", 0.0048544897806762875),
            ("Doris", 0.004804700141900737),
            ("Yovana", 0.004779805322512181),
            ("Gloria", 0.004754910503123625),
            ("Yesenia", 0.004754910503123625),
            ("Rocío", 0.00473001568373663),
            ("Margarita", 0.004705120864348074),
            ("Valeria", 0.004680226044959518),
            ("Mónica", 0.004505962309242749),
            ("Mercedes", 0.004456172670467199),
            ("María Teresa", 0.004456172670467199),
            ("Jenny", 0.00433169857352598),
            ("Noemi", 0.0042570141153618745),
            ("Martha", 0.004207224476586324),
            ("Evelyn", 0.004132540018422217),
            ("Carla", 0.004132540018422217),
            ("Rosa Maria", 0.004107645199033661),
            ("Rosa Isabel", 0.004107645199033661),
            ("Lisbeth", 0.004082750379645105),
            ("Cristina", 0.004057855560258111),
            ("Janeth", 0.0040329607408695544),
            ("Hilda", 0.003983171102094004),
            ("Sara", 0.003983171102094004),
            ("Elena", 0.003883591824541342),
            ("Mary Carmen", 0.003883591824541342),
            ("Elsa", 0.0038338021857642294),
            ("Diana Elizabeth", 0.0038338021857642294),
            ("Lidia", 0.0038338021857642294),
            ("Veronica", 0.0038338021857642294),
            ("Mary Luz", 0.0037840125469886794),
            ("Delia", 0.0037840125469886794),
            ("Yessica", 0.003709328088824573),
            ("Susana", 0.003709328088824573),
            ("Olga", 0.003709328088824573),
            ("Juana", 0.003684433269436017),
            ("Lorena", 0.0036346436306604665),
            ("Natalia", 0.0036346436306604665),
            ("María José", 0.0036346436306604665),
            ("Fabiola", 0.003584853991883355),
            ("María", 0.003584853991883355),
            ("Deysi", 0.003535064353107804),
            ("Ana Lucía", 0.003535064353107804),
            ("Laura", 0.003535064353107804),
            ("Rosa Luz", 0.003460379894943698),
            ("Adriana", 0.003435485075555142),
            ("Victoria", 0.003435485075555142),
            ("Violeta", 0.0033856954367795914),
            ("Dina", 0.003360800617391035),
            ("Irma", 0.003335905798002479),
            ("Mirian", 0.003311010978615485),
            ("María Esther", 0.003286116159226929),
            ("Julia", 0.003286116159226929),
            ("María Elizabeth", 0.0032612213398383726),
            ("Janet", 0.0032612213398383726),
            ("Marleni", 0.0032612213398383726),
            ("Yaneth", 0.0032612213398383726),
            ("Pilar", 0.003211431701062822),
            ("Ana Claudia", 0.003211431701062822),
            ("Mariana", 0.0031616420622872722),
            ("María Cristina", 0.0031616420622872722),
            ("Marlene", 0.0031367472428987164),
            ("Ana", 0.0031367472428987164),
            ("Bertha", 0.00311185242351016),
            ("Angela", 0.00311185242351016),
            ("Soledad", 0.00311185242351016),
            ("Fiorela", 0.003086957604121604),
            ("Jackeline", 0.0030620627847346097),
            ("Mariluz", 0.0030371679653460534),
            ("Tatiana", 0.0030122731459574976),
            ("María Angélica", 0.0029873783265705034),
            ("Maria Luisa", 0.0029873783265705034),
            ("Nilda", 0.0029873783265705034),
            ("Karla", 0.0029873783265705034),
            ("Yesica", 0.002962483507181947),
            ("Luz María", 0.002962483507181947),
            ("Rosa Elvira", 0.002962483507181947),
            ("Cynthia", 0.002937588687793391),
            ("Eliana", 0.002937588687793391),
            ("Lizeth", 0.0029126938684063968),
            ("Jacqueline", 0.002862904229629285),
            ("Nataly", 0.002862904229629285),
            ("Lucy", 0.002838009410240729),
            ("Giovanna", 0.002838009410240729),
            ("Lucero", 0.002838009410240729),
            ("Teresa", 0.0028131145908537342),
            ("Rosa Elena", 0.0028131145908537342),
            ("Mery", 0.0028131145908537342),
            ("Maria Teresa", 0.0027882197714651784),
            ("Camila", 0.002738430132689628),
            ("Viviana", 0.002738430132689628),
            ("Ana Gabriela", 0.002738430132689628),
            ("Celia", 0.002713535313301072),
            ("Gisela", 0.0026637456745255217),
            ("Wendy", 0.0026637456745255217),
            ("Ana Rosa", 0.002613956035748409),
            ("Alessandra", 0.002613956035748409),
            ("Lucia", 0.0025890612163598534),
            ("Betty", 0.0025890612163598534),
            ("Yeny", 0.0025890612163598534),
            ("Margot", 0.002539271577584303),
            ("Graciela", 0.002514376758195747),
            ("Marina", 0.002514376758195747),
            ("María Eugenia", 0.0024645871194201967),
            ("Katia", 0.0024645871194201967),
            ("Shirley", 0.0024645871194201967),
            ("Ana Isabel", 0.0024396923000316404),
            ("Sandra Paola", 0.0024396923000316404),
            ("Noemí", 0.0024147974806446467),
            ("Monica", 0.0024147974806446467),
            ("María Claudia", 0.0024147974806446467),
            ("Claudia Alejandra", 0.0024147974806446467),
            ("Ximena", 0.0024147974806446467),
            ("Julissa", 0.0023899026612560904),
            ("María Mercedes", 0.0023899026612560904),
            ("Angélica María", 0.002365007841867534),
            ("Fanny", 0.002365007841867534),
            ("Yessenia", 0.002365007841867534),
            ("Vanesa", 0.002340113022478978),
            ("Maria Elizabeth", 0.0023152182030919837),
            ("Brenda", 0.002265428564314872),
            ("Ana Paola", 0.002265428564314872),
            ("Jimena", 0.002265428564314872),
            ("Maria Cristina", 0.0022405337449278775),
            ("Maria", 0.0022405337449278775),
            ("Elisa", 0.002215638925539321),
            ("Maria Jose", 0.002215638925539321),
        ]
    )

    @property
    def first_names(self):
        """Returns a list of weighted first names, male and female."""
        if not hasattr(self, "_first_names"):
            self._first_names = OrderedDict()
            for a, b in zip_longest(
                self.first_names_male.items(), self.first_names_female.items()
            ):
                if a is not None:
                    name, weight = a
                    self._first_names[name] = weight / 2
                if b is not None:
                    name, weight = b
                    self._first_names[name] = weight / 2
        return self._first_names

    # 500 last names, weighted
    last_names = OrderedDict(
        [
            ("Quispe", 0.029628),
            ("Flores", 0.023719),
            ("Rojas", 0.019469),
            ("Torres", 0.017041),
            ("Ramos", 0.014979),
            ("Mendoza", 0.014184),
            ("Espinoza", 0.013910),
            ("Sánchez", 0.013693),
            ("Gonzales", 0.013560),
            ("Mamani", 0.013398),
            ("Rodríguez", 0.012310),
            ("Castillo", 0.012288),
            ("García", 0.012278),
            ("Vargas", 0.012233),
            ("Rodriguez", 0.011387),
            ("Vásquez", 0.010897),
            ("Cruz", 0.010280),
            ("Díaz", 0.010152),
            ("Ruiz", 0.010001),
            ("López", 0.009926),
            ("Sanchez", 0.009672),
            ("Pérez", 0.009601),
            ("Romero", 0.009564),
            ("Castro", 0.009341),
            ("Diaz", 0.009190),
            ("Garcia", 0.008877),
            ("Salazar", 0.008829),
            ("Chávez", 0.008678),
            ("Paredes", 0.008619),
            ("Rivera", 0.008530),
            ("Silva", 0.008516),
            ("Medina", 0.008329),
            ("Ramirez", 0.007979),
            ("Ramírez", 0.007949),
            ("Morales", 0.007893),
            ("Aguilar", 0.007872),
            ("Vasquez", 0.007584),
            ("Herrera", 0.007552),
            ("Delgado", 0.007529),
            ("Fernández", 0.007523),
            ("Huamán", 0.007333),
            ("Palomino", 0.007303),
            ("Huaman", 0.007216),
            ("Reyes", 0.007193),
            ("Lopez", 0.007155),
            ("Perez", 0.007154),
            ("Chavez", 0.007120),
            ("Gutierrez", 0.006591),
            ("Condori", 0.006266),
            ("Campos", 0.006200),
            ("Vega", 0.006193),
            ("Soto", 0.006090),
            ("Alvarado", 0.006012),
            ("Muñoz", 0.005983),
            ("Villanueva", 0.005957),
            ("Guevara", 0.005629),
            ("Alvarez", 0.005546),
            ("Ortiz", 0.005498),
            ("Fernandez", 0.005432),
            ("Peña", 0.005382),
            ("León", 0.005316),
            ("Cabrera", 0.005117),
            ("Gómez", 0.005019),
            ("Saavedra", 0.005009),
            ("Meza", 0.005003),
            ("Gutiérrez", 0.004806),
            ("Guerrero", 0.004733),
            ("Salas", 0.004701),
            ("Vera", 0.004623),
            ("Navarro", 0.004466),
            ("Miranda", 0.004461),
            ("Palacios", 0.004457),
            ("Apaza", 0.004395),
            ("Moreno", 0.004382),
            ("Córdova", 0.004265),
            ("Gomez", 0.004226),
            ("Martínez", 0.004199),
            ("Rios", 0.004183),
            ("Contreras", 0.004167),
            ("Martinez", 0.004021),
            ("Calderón", 0.003993),
            ("Sandoval", 0.003981),
            ("Vilca", 0.003957),
            ("Cárdenas", 0.003934),
            ("Nuñez", 0.003897),
            ("Pacheco", 0.003836),
            ("Carrasco", 0.003824),
            ("Jara", 0.003778),
            ("Zapata", 0.003774),
            ("Aguirre", 0.003730),
            ("Valdivia", 0.003676),
            ("Bravo", 0.003667),
            ("Cordova", 0.003644),
            ("Quiroz", 0.003593),
            ("Arias", 0.003555),
            ("Lozano", 0.003538),
            ("Huamani", 0.003456),
            ("Castañeda", 0.003415),
            ("Tello", 0.003413),
            ("Tapia", 0.003381),
            ("Valencia", 0.003372),
            ("Luna", 0.003322),
            ("Rosales", 0.003322),
            ("Cueva", 0.003274),
            ("Ayala", 0.003248),
            ("Gamarra", 0.003241),
            ("Leon", 0.003225),
            ("Velásquez", 0.003214),
            ("Guerra", 0.003205),
            ("Dávila", 0.003203),
            ("Velasquez", 0.003191),
            ("Bustamante", 0.003175),
            ("Figueroa", 0.003175),
            ("Ríos", 0.003066),
            ("Pinedo", 0.003004),
            ("Jiménez", 0.002977),
            ("Hidalgo", 0.002977),
            ("Acosta", 0.002974),
            ("Cardenas", 0.002967),
            ("Saldaña", 0.002926),
            ("Jimenez", 0.002924),
            ("Santos", 0.002915),
            ("Alva", 0.002913),
            ("Hernández", 0.002908),
            ("nan", 0.002901),
            ("Trujillo", 0.002872),
            ("Hurtado", 0.002867),
            ("Zevallos", 0.002846),
            ("Vela", 0.002832),
            ("Ponce", 0.002823),
            ("Salinas", 0.002800),
            ("Carranza", 0.002751),
            ("Zegarra", 0.002746),
            ("Valverde", 0.002739),
            ("Carbajal", 0.002739),
            ("Peralta", 0.002727),
            ("Cornejo", 0.002703),
            ("Bautista", 0.002657),
            ("Paucar", 0.002655),
            ("Becerra", 0.002652),
            ("Núñez", 0.002618),
            ("Choque", 0.002597),
            ("Alarcón", 0.002583),
            ("Cáceres", 0.002568),
            ("Rivas", 0.002545),
            ("Villegas", 0.002545),
            ("Guzmán", 0.002536),
            ("Ochoa", 0.002535),
            ("Mejía", 0.002524),
            ("Ortega", 0.002515),
            ("Acuña", 0.002513),
            ("Robles", 0.002511),
            ("Benites", 0.002462),
            ("Alfaro", 0.002460),
            ("Montoya", 0.002422),
            ("Manrique", 0.002405),
            ("Calderon", 0.002392),
            ("Rengifo", 0.002376),
            ("Estrada", 0.002366),
            ("Correa", 0.002360),
            ("Aliaga", 0.002293),
            ("Huanca", 0.002282),
            ("Lazo", 0.002280),
            ("Suarez", 0.002277),
            ("Paz", 0.002248),
            ("Ticona", 0.002245),
            ("Poma", 0.002204),
            ("Zavaleta", 0.002202),
            ("Loayza", 0.002200),
            ("Aquino", 0.002177),
            ("Arroyo", 0.002175),
            ("Ventura", 0.002166),
            ("Caballero", 0.002150),
            ("Molina", 0.002136),
            ("Angulo", 0.002129),
            ("Inga", 0.002122),
            ("Solis", 0.002115),
            ("Maldonado", 0.002109),
            ("Mejia", 0.002069),
            ("Arce", 0.002065),
            ("Linares", 0.002051),
            ("Cubas", 0.002036),
            ("Carrillo", 0.002036),
            ("Calle", 0.002031),
            ("Vidal", 0.002022),
            ("Osorio", 0.002012),
            ("Sosa", 0.002008),
            ("Fuentes", 0.001996),
            ("Padilla", 0.001994),
            ("Escobar", 0.001992),
            ("Tejada", 0.001985),
            ("Davila", 0.001983),
            ("Araujo", 0.001983),
            ("Prado", 0.001958),
            ("Vilchez", 0.001948),
            ("Salcedo", 0.001946),
            ("Mori", 0.001944),
            ("Llanos", 0.001935),
            ("Gonzáles", 0.001921),
            ("Rosas", 0.001907),
        ]
    )

    prefixes_male = ("Sr.", "Dr.", "Don")
    prefixes_female = ("Srta.", "Sra.", "Dra.", "Doña")

    def name(self) -> str:
        # Select format, then generate name
        format: str = self.random_element(self.formats)
        pattern: str = self.random_element(getattr(self, format))
        return self.generator.parse(pattern)

    def given_name(self) -> str:
        """Generates a composite given name with two unique names"""
        if self.random_int(0, 1) == 1:
            source = self.first_names_female
        else:
            source = self.first_names_male
        names = self.random_elements(source, length=2, unique=True)  # type: ignore[var-annotated]
        return " ".join(names)

    def given_name_male(self) -> str:
        """Generates a composite male given name with two unique names"""
        names = self.random_elements(self.first_names_male, length=2, unique=True)  # type: ignore[var-annotated]
        return " ".join(names)

    def given_name_female(self) -> str:
        """Generates a composite female given name with two unique names"""
        names = self.random_elements(self.first_names_female, length=2, unique=True)  # type: ignore[var-annotated]
        return " ".join(names)
