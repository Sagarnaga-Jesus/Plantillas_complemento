from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import re

app = Flask(__name__)

app.config["SECRET_KEY"]="1q2w3e4r5t6y7u8i9o0p"
app.secret_key="1q2w3e4r5t6y7u8i9o0pazsxdcfvgbhnjmkl"
#@app.permanent session lifetime =  timedelta(minutes=5)
#@app.permanent = True

personas = []

@app.route("/login/<username>")#registra sesión
def login(username):
    session['username'] = username
    return f"Hola, {username}! Has iniciado sesión correctamente."

@app.route("/perfil")#muestra perfil de usuario o inicia secion
def profile():
    username = session.get('username')
    if username is not None:
        return "user: " + username
    return "Not logged in!"

@app.route("/logout")#cierra sesión
def logout():
    session.pop('username', None)
    return "Has cerrado sesión correctamente."



@app.route("/sesion")
def index():
    
    return render_template("base2.html")

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/animales_exoticos")
def animales():
    animales = [
            {"nombre":"Tapir (Tapirus) ",
            "informacion":"El tapir es un mamífero grande y herbívoro que habita en zonas boscosas de américa del sur, américa central y el sudeste asiático. Se trata de una de las familias más antiguas desde hace unos 55 millones de años, lo que lo convierte en uno de los animales exóticos del mundo.",
            "imagen":"/static/imagenes/tapir_tapirus_3774_2_600.webp",
            "tipo":"Terrestre"
            },
            
            {"nombre":"Escalopendra gigante (Scolopendra gigantea)",
            "informacion":"La escalopendra gigante o Scolopendra gigantea es una especie de ciempiés gigante que se encuentra en las tierras bajas de Venezuela, Colombia, islas de Trinidad y Jamaica. Se trata de un animal carnívoro que se alimenta de reptiles, anfibios, e incluso mamíferos como ratones y murciélagos.",
            "imagen":"static/imagenes/escalopendra_gigante_scolopendra_gigantea_3774_4_600.webp",
            "tipo":"Terrestre"
            },
            
            {"nombre":"Dragones de mar (Phycodurus eques)",
            "informacion":"Los dragones de mar son peces marinos que se encuentran en las aguas costeras de Australia. Son conocidos por su apariencia única, que se asemeja a la de un caballo de mar, y por su capacidad para camuflarse entre las algas y los corales.",
            "imagen":"static/imagenes/dragones_de_mar_phycodurus_eques_3774_5_600.webp",
            "tipo":"Acuático"
            },
            {"nombre":"Cangrejo yeti (Kiwa hirsuta)",
            "informacion":"El cangrejo yeti, descubierto en 2005 cerca de la isla de Pascua, es un crustáceo ciego que vive a grandes profundidades, cubierto de filamentos sedosos que albergan bacterias, cuya función podría ser protegerlo de sustancias tóxicas en su entorno.",
            "imagen":"static/imagenes/1677794326_511_Cangrejo-Yeti-El-cangrejo-blanco-mas-extrano-del-mar.webp",
            "tipo":"Acuático"
            },
            {"nombre":"Lémures voladores",
            "informacion":"También se les llama colugos y, fuera de los murciélagos, son los mamíferos más altamente adaptados para el vuelo. Como puedes ver, sus miembros y cola están conectados por colgajos de piel que se conectan a los confines de sus extremidades, aumentando así su superficie y convirtiéndolos en mejores planeadores. Puede deslizarse hasta 3230 pies, casi sin pérdida de altura.",
            "imagen":"static/imagenes/lemur-volador.jpg",
            "tipo":"Volador"
            },
            {"nombre":"El colibrí zunzuncito",
            "informacion":"El colibrí zunzuncito, también conocido como el colibrí abeja, es el ave más pequeña del mundo. Mide aproximadamente 2.2 pulgadas de longitud y pesa alrededor de 1.6 gramos. Se encuentra principalmente en Cuba y la Isla de la Juventud. La especie ha sido clasificada como casi amenazada por la (UICN) debido a una población estimada entre 22 000 y 66 000 individuos maduros que está en declive moderadamente rápido, principalmente por la pérdida y degradación de su hábitat",
            "imagen":"static/imagenes/512px-Bee_hummingbird_(Mellisuga_helenae)_adult_male_in_flight-cropped.webp",
            "tipo":"Volador"
            }
            
        ]
    return render_template("animales.html", animal=animales)

@app.route("/vehiculos_antiguos")
def vehiculos():
    vehiculos = [
        {"nombre":"Ford Mustang Fastback de 1969",
        "informacion":"Modelo perteneciente a la primera generación del automóvil, producido entre 1968 y 1970, con una longitud de 4,762 mm y una distancia entre ejes de 2,743 mm. Este modelo se fabricó en varias ubicaciones, incluyendo Dearborn, Michigan, Milpitas, California, Metuchen, Nueva Jersey, Valencia, Venezuela y Ciudad de México. Fue diseñado por Gale Halderman, quien también fue responsable del diseño del primer Mustang.",
        "imagen":"static/imagenes/1969-ford-mustang.jpg",
        },
        {"nombre":"Chevrolet Bel Air",
        "informacion":"El Chevrolet Bel Air es un automóvil clásico que se produjo en varias generaciones desde 1950 hasta 1981. Es conocido por su diseño elegante y su rendimiento en la carretera. El modelo de 1950, en particular, es muy apreciado por los coleccionistas. el nombre Bel Air se aplicó únicamente a los modelos de dos puertas tipo hardtop, diferenciándolos de los modelos Styleline y Fleetline.",
        "imagen":"static/imagenes/Chevrolet-Bel-Air-1950.webp",
        },
        {"nombre":"Volkswagen Combi Alemana de 1972",
        "informacion":"La Volkswagen Combi, también conocida como Volkswagen Type 2 o VW Bus, es un vehículo icónico que se produjo desde 1950. La versión de 1972 es especialmente apreciada por su diseño retro y su versatilidad como vehículo familiar y de transporte.",
        "imagen":"static/imagenes/512px-0385_Porsche_Diesel_Bus_blau.webp"
        },
        {"nombre":"Cadillac Eldorado de 1959",
        "informacion":" El Cadillac Eldorado (1959) pertenece a la quinta generación. Este modelo es totalmente diferente a los Cadillacs de la generación pasada. Su motor es tipo V8 con una cilindrada de 6382 cm3. Posee 16 válvulas, 3 velocidades automáticas en la caja de cambios. Es un coche totalmente ecológico ya que no emite CO2. Cuenta con una carrocería de acero tipo Cabriolet con dos puertas.",
        "imagen":"static/imagenes/Cadillac_Eldorado-1959-800x400.webp"
        },
        {"nombre":"Dodge Charger de 1968",
        "informacion":"El Dodge Charger de 1968 es un automóvil deportivo que se ha convertido en un ícono de la cultura automotriz estadounidense. Con su diseño agresivo y potente motor, el Charger ha dejado una huella imborrable en la historia del automovilismo.",
        "imagen":"static/imagenes/512px-Dodge.383.magnum-black.front.view-sstvwf.webp"
        }
    ]
    return render_template("vehiculos.html", vehiculos=vehiculos)

@app.route("/maravillas_mundo")
def maravillas():
    
    maravillas = [
        {"nombre":"Gran Muralla China",
        "informacion":"La Gran Muralla China es una antigua estructura defensiva que se extiende a lo largo de miles de kilómetros en el norte de China. Fue construida para proteger el imperio chino de invasiones y ataques de tribus nómadas. La muralla es una maravilla arquitectónica y un símbolo de la historia y la cultura chinas.",
        "imagen":"static/imagenes/360_F_301737869_7WaGBgmHO5kQ0qNpbCADl0nyYNd66814.webp",
        },
        {"nombre":"Machu Picchu",
        "informacion":"Machu Picchu es una antigua ciudad inca ubicada en las montañas de Perú. Fue construida en el siglo XV y es conocida por su arquitectura impresionante y su ubicación espectacular en la cima de una montaña. Machu Picchu es un sitio arqueológico importante y un destino turístico popular.",
        "imagen":"static/imagenes/machu-picchu-peru.webp",
        },
        {"nombre":"Taj Mahal",
        "informacion":"El Taj Mahal es un mausoleo ubicado en Agra, India. Fue construido en el siglo XVII por el emperador mogol Shah Jahan en memoria de su esposa favorita, Mumtaz Mahal. El Taj Mahal es conocido por su arquitectura impresionante, que combina elementos islámicos, persas e indios, y es considerado una de las maravillas del mundo.",
        "imagen":"static/imagenes/taj-mahal-agra-india-s-iconic-seen-mosque-just-west-mausoleum-34386153.webp",
        },
        {"nombre":"Coliseo Romano",
        "informacion":"El Coliseo Romano es un anfiteatro ubicado en Roma, Italia. Fue construido en el siglo I d.C. y es conocido por su arquitectura impresionante y su historia como lugar de entretenimiento para los antiguos romanos. El Coliseo es uno de los monumentos más emblemáticos de Roma y un símbolo de la antigua civilización romana.",
        "imagen":"static/imagenes/colosseum-rome.webp",
        },
        {"nombre":"Cristo Redentor",
        "informacion":"El Cristo Redentor es una estatua gigante ubicada en Río de Janeiro, Brasil. Fue construida en la década de 1930 y representa a Jesucristo con los brazos extendidos. La estatua es un símbolo importante de Brasil y ofrece vistas panorámicas impresionantes de la ciudad desde su ubicación en la cima del cerro del Corcovado.",
        "imagen":"static/imagenes/famous-christ-the-redeemer-in-downtown-rio-de-janeiro-brazil.webp",
        },
        {"nombre":"Petra",
        "informacion":"Petra es una antigua ciudad nabatea ubicada en Jordania. Fue construida en el siglo IV a.C. y es conocida por su arquitectura impresionante, que incluye templos, tumbas y edificios tallados en la roca. Petra es un sitio arqueológico importante y un destino turístico popular.",
        "imagen":"static/imagenes/petra-jordan34-940x627.webp",   
        },
        {"nombre":"Chichén Itzá",
        "informacion":"Chichén Itzá es una antigua ciudad maya ubicada en la península de Yucatán, México. Fue un importante centro político, económico y religioso durante la civilización maya. Chichén Itzá es famosa por su arquitectura impresionante, que incluye la pirámide de Kukulkán, el observatorio astronómico y el juego de pelota. Es un sitio arqueológico declarado Patrimonio de la Humanidad por la UNESCO.",
        "imagen":"static/imagenes/chichen-itza-yucatan-mexico.webp",
        }
    ]

    return render_template("maravillas.html", maravillas=maravillas)

@app.route("/acerca_de")
def acerca():
    return render_template("acerca.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/datos", methods=["POST", "GET"])
def datos():
    
    error =  None
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        contacto = request.form["contacto"]
        contraseña = request.form["contraseña"]
        dia = request.form["dia"]
        mes = request.form["meses"]
        año = request.form["año"]
        genero = request.form["genero"]
        
        persona ={"name": nombre,
            "apellido": apellido,
            "contacto": contacto,
            "contraseña": contraseña,
            "dia": dia,
            "mes": mes,
            "año": año,
            "genero": genero
            }
        personas.append(persona)
        
        if nombre == "nombre":
            error = "favor de rellenar con informacion valida nombre"
            if  error != None:
                flash(error, "danger")
                return render_template(("formulario.html"))
            else:
                flash(f"¡Formulario enviado con éxito! para: {nombre}", "success")
                return render_template("base2.html")
            
        if apellido == "apellido":
            error = "favor de rellenar con informacion valida apellido"
            if  error != None:
                flash(error, "danger")
                return render_template(("formulario.html"))
            else:
                flash(f"¡Formulario enviado con éxito! para: {nombre}", "success")
                return render_template("base2.html")
        
        if contraseña == "contraseña":
            error = "Utilice informacion valida"
            if  error != None:
                flash(error, "danger")
                return render_template(("formulario.html"))
            else:
                flash(f"¡Formulario enviado con éxito! para: {nombre}", "success")
                return render_template("base2.html")

        año_num = int(año)
        hoy = datetime.now()
        edad = hoy.year - año_num
        
        if edad < 18:
            error = "Debes ser mayor de edad para registrarte."
            if  error != None:
                flash(error, "danger")
                return render_template(("formulario.html"))
            else:
                flash(f"¡Formulario enviado con éxito! para: {nombre}", "success")
                return render_template("base2.html")
            
        
        patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        correo = re.match(patron_correo, contacto)
        numero = contacto.isdigit() and len(contacto) == 10

        if not correo and not numero:
            flash("El número o correo electrónico es inválido.", "danger")
            return render_template("formulario.html")
        else:
            flash(f"¡Formulario enviado con éxito! para: {nombre}", "success")
            return render_template("base2.html")
        


@app.route("/sesion", methods=["POST", "GET"])
def sesion():
    error =  None
    if request.method == "POST":
        contacto = request.form["contacto"]
        contraseña = request.form["contraseña"]
        
        for persona in personas:
            if persona["contacto"] == contacto and persona["contraseña"] == contraseña:
                usuario_encontrado = persona
                break

        
        if contraseña != usuario_encontrado["contraseña"]:
            error = "Las contraseñas no coinciden. Por favor, inténtalo de nuevo. O no"
            if  error != None:
                flash(error, "danger")
                return render_template(("base2.html"))
            else:
                flash(f"¡Sesion iniciada con éxito! para: {contacto}", "success")
            return render_template("inicio.html")

        if usuario_encontrado["contacto"]!=contacto:
            flash(f"El número o correo electrónico es inválido.", "danger")
            return render_template("base2.html")
        else:
            flash(f"¡Sesion iniciada con éxito! para: {contacto}", "success")
            return render_template("inicio.html")
        
    return render_template("inicio.html")

@app.route("/cerrar_sesion")
def cerrar_sesion():
    session.pop('username', None)
    return render_template("base2.html")



if __name__ == "__main__":
    app.run(debug=True)