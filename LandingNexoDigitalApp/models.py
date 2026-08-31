from django.db import models

# Create your models here.
class ResumenServicios():
    def __init__(self, url, icon, title, text):
        self.url = url
        self.icon = icon
        self.title = title
        self.text = text

def resumenServicios():
    lista_resumen = [
        ResumenServicios('web' ,'WEB', 'Desarrollo de Sitios Web', 'Sitios y aplicaciones web a medida, rápidos y responsivos para tu negocio.'),
        ResumenServicios('mobile', 'APP', 'Aplicaciones Móviles', 'Apps nativas e híbridas para Android e iOS, conectadas a tus sistemas.'), 
        ResumenServicios('nube', 'CLOUD', 'Consultoría en la Nube', 'Migración y optimización de infraestructura en la nube para tu empresa.'),
        ResumenServicios('seguridad', 'SEC', 'Ciberseguridad para Pymes', 'Protege los datos de tu empresa y de tus clientes con buenas prácticas reales.'), 
    ]
    return lista_resumen

class Servicios():
    def __init__(self, nombre, resumen, descripcion, caracteristicas, precio, duracion):
        self.nombre = nombre
        self.resumen = resumen
        self.descripcion = descripcion
        self.caracteristicas = caracteristicas
        self.precio = precio
        self.duracion = duracion

def serviciosWeb():
    
    lista_servicios = [
        Servicios('Desarrollo de Sitios Web',
                  'Sitios y aplicaciones web a medida, rápidos y responsivos para tu negocio.',
                  'Diseñamos y desarrollamos sitios web y aplicaciones a medida para empresas que necesitan presencia digital profesional. Trabajamos con tecnologías modernas del lado del servidor para que tu sitio sea rápido, seguro y fácil de mantener.',
                  ['Diseño responsivo para escritorio, tablet y móvil',
                   'Panel de administración de contenidos',
                   'Optimización de velocidad de carga',
                   'Integración con redes sociales y formularios de contacto'
                   ],
                  'Desde $450.000',
                  'Plazo estimado: 3 a 6 semanas'),
    ]
    return lista_servicios

def serviciosMobiles():
    
    lista_servicios = [
        Servicios('Aplicaciones Móviles',
                  'Apps nativas e híbridas para Android e iOS, conectadas a tus sistemas.',
                  'Desarrollamos aplicaciones móviles para Android e iOS conectadas a tus sistemas de backend existentes, pensadas para acompañar a tus clientes desde el celular con la misma calidad que tu plataforma web.',
                  ['Apps nativas e híbridas (Android / iOS)',
                   'Notificaciones push y geolocalización',
                   'Conexión a API REST propia o de terceros',
                   'Publicación en Google Play y App Store',
                   ],
                  'Desde $890.000',
                  'Plazo estimado: 6 a 10 semanas'),

    ]
    return lista_servicios

def serviciosNube():
    
    lista_servicios = [
        Servicios('Consultoría en la Nube',
                  'Migración y optimización de infraestructura en la nube para tu empresa.',
                  'Ayudamos a tu empresa a migrar y optimizar su infraestructura en servicios en la nube, reduciendo costos operativos y mejorando la disponibilidad de tus sistemas críticos.',
                  ['Diagnóstico de infraestructura actual',
                   'Migración de servidores y bases de datos',
                   'Configuración de respaldos automáticos',
                   'Monitoreo y alertas 24/7'   
                    ],
                  'Desde $600.000',
                  'Plazo estimado: 2 a 4 semanas'),

    ]
    return lista_servicios

def serviciosSeguridad():
    
    lista_servicios = [
                Servicios('Ciberseguridad para Pymes',
                  'Protege los datos de tu empresa y de tus clientes con buenas prácticas reales.',
                  'Evaluamos la seguridad de tus sistemas y aplicamos buenas prácticas de protección de datos, control de accesos y respuesta ante incidentes, adaptadas a la realidad de una pyme.',
                  ['Auditoría básica de vulnerabilidades',
                   'Políticas de contraseñas y control de accesos',
                   'Respaldo y recuperación ante incidentes',
                   'Capacitación al equipo interno'
                    ],
                  'Desde $350.000',
                  'Plazo estimado: 2 a 3 semanas'),
    ]
    return lista_servicios
