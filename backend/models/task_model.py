import re
from backend.models.connection_pool import MySQLPool


class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

#cocina
###################################################

    def get_kitchen(self, ID_cocina):
        params = {'ID_cocina' : ID_cocina}
        rv = self.mysql_pool.execute("SELECT * from cocina where ID_cocina=%(ID_cocina)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'ID_cocina': result[0], 'ID_categoria': result[1], 'Marca': result[2], 'Nombre': result[3], 'Precio': result[4], 'Stock': result[5], 'Descripcion': result[6]}
            data.append(content)
            content = {}
        return data

    def get_kitchens(self):
        rv = self.mysql_pool.execute("SELECT * from cocina")
        data = []
        content = {}
        for result in rv:
            content = {'ID_cocina': result[0], 'ID_categoria': result[1], 'Marca': result[2], 'Nombre': result[3], 'Precio': result[4], 'Stock': result[5], 'Descripcion': result[6]}
            data.append(content)
            content = {}
        return data

    def add_kitchen(self, Marca, Nombre, Precio, Stock, Descripcion):    
        params = {
            'Marca' : Marca,
            'Nombre' : Nombre,
            'Precio' : Precio,
            'Stock' : Stock,
            'Descripcion' : Descripcion
        } 
        query = """INSERT INTO cocina (Marca, Nombre, Precio, Stock, Descripcion) 
            values (%(Marca)s, %(Nombre)s, %(Precio)s, %(Stock)s, %(Descripcion)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'ID_cocina': cursor.lastrowid, 'Marca': Marca, 'Nombre': Nombre, 'Precio': Precio, 'Stock': Stock, 'Descripcion': Descripcion}
        return data

    def delete_kitchen(self, ID_cocina):    
        params = {'ID_cocina' : ID_cocina}      
        query = """delete from cocina where ID_cocina = %(ID_cocina)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


#Especificaciones
###################################################


    def get_specification(self, ID_especificaciones):
        params = {'ID_especificaciones' : ID_especificaciones}      
        rv = self.mysql_pool.execute("SELECT * from Especificaciones where ID_especificaciones=%(ID_especificaciones)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'ID_especificaciones': result[0], 'Numero_de_quemadores': result[1], 'Material_de_la_parrilla': result[2],
                         'Material_de_la_cubierta': result[3], 'Capacidad_del_horno': result[4], 
                         'Encendido_electronico': result[5], 'Tipo_de_energia' : result[6], 'Timer': result[7], 'Incluye_tapa': result[8],
                         'Marca': result[9], 'Modelo': result[10], 'Tipo': result[11], 'Alto': result[12], 'Ancho': result[13], 
                         'Profundidad': result[14], 'Peso': result[15], 'Hecho_en': result[16]}
            data.append(content)
            content = {}
        return data

    def get_specifications(self):  
        rv = self.mysql_pool.execute("SELECT * from Especificaciones")  
        data = []
        content = {}
        for result in rv:
            content = {'ID_cocina': result[0], 'Numero_de_quemadores': result[1], 'Material_de_la_parrilla': result[2], 
                        'Material_de_la_cubierta': result[3], 'Capacidad_del_horno': result[4], 
                        'Encendido_electronico': result[5], 'Tipo_de_energia' : result[6], 'Timer': result[7], 'Incluye_tapa': result[8],
                         'Marca': result[9], 'Modelo': result[10], 'Tipo': result[11], 'Alto': result[12], 'Ancho': result[13], 
                         'Profundidad': result[14], 'Peso': result[15], 'Hecho_en': result[16]}
            data.append(content)
            content = {}
        return data

    def add_specification(self,ID_cocina,Numero_de_quemadores,Material_de_la_parrilla,Material_de_la_cubierta,Capacidad_del_horno,Encendido_electronico,Tipo_de_energia,Timer,Incluye_tapa,Marca,Modelo,Tipo,Alto,Ancho,Profundidad,Peso,Hecho_en):    
        params = {
            'ID_cocina' : ID_cocina,
            'Numero_de_quemadores' : Numero_de_quemadores,
            'Material_de_la_parrilla' : Material_de_la_parrilla,
            'Material_de_la_cubierta' : Material_de_la_cubierta,
            'Capacidad_del_horno' : Capacidad_del_horno,
            'Encendido_electronico' : Encendido_electronico,
            'Tipo_de_energia' : Tipo_de_energia,
            'Timer' : Timer,
            'Incluye_tapa' : Incluye_tapa,
            'Marca' : Marca,
            'Modelo' : Modelo,
            'Tipo' : Tipo,
            'Alto' : Alto,
            'Ancho' : Ancho,
            'Profundidad' : Profundidad,
            'Peso' : Peso,
            'Hecho_en' : Hecho_en
        }
        query = """INSERT INTO Especificaciones (ID_cocina,Numero_de_quemadores,Material_de_la_parrilla,Material_de_la_cubierta,Capacidad_del_horno,Encendido_electronico,Tipo_de_energia,Timer,Incluye_tapa,Marca,Modelo,Tipo,Alto,Ancho,Profundidad,Peso,Hecho_en) 
            values (%(ID_cocina)s, %(Numero_de_quemadores)s, %(Material_de_la_parrilla)s, %(Material_de_la_cubierta)s, %(Capacidad_del_horno)s, %(Encendido_electronico)s, %(Tipo_de_energia)s, %(Timer)s, %(Incluye_tapa)s, %(Marca)s, %(Modelo)s, %(Tipo)s, %(Alto)s, %(Ancho)s, %(Profundidad)s, %(Peso)s, %(Hecho_en)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'ID_especificaciones': cursor.lastrowid, 'ID_cocina': ID_cocina, 'Numero_de_quemadores': Numero_de_quemadores,
                 'Material_de_la_parrilla': Material_de_la_parrilla, 'Material_de_la_cubierta': Material_de_la_cubierta,
                  'Capacidad_del_horno': Capacidad_del_horno, 'Encendido_electronico' : Encendido_electronico, 'Tipo_de_energia' : Tipo_de_energia, 
                  'Timer' : Timer, 'Incluye_tapa' : Incluye_tapa, 'Marca' : Marca, 'Modelo' : Modelo, 'Tipo' : Tipo, 'Alto' : Alto, 'Ancho' : Ancho, 
                  'Profundidad' : Profundidad, 'Peso' : Peso, 'Hecho_en' : Hecho_en}
        return data

    def delete_specification(self, ID_especificaciones):    
        params = {'ID_especificaciones' : ID_especificaciones}      
        query = """delete from Especificaciones where ID_cocina = %(ID_especificaciones)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data



#User
###################################################

    def get_user(self, DNI): 
        params = {'DNI' : DNI}
        rv = self.mysql_pool.execute("SELECT * from user where DNI=%(DNI)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'Username': result[0], 'Password': result[1]}
            data.append(content)
            content = {}
        return data

    def get_users(self):  
        rv = self.mysql_pool.execute("SELECT * from user")  
        data = []
        content = {}
        for result in rv:
            content = {'DNI': result[0], 'Username': result[1], 'Password': result[2]}
            data.append(content)
            content = {}
        return data

    def add_user(self, Username, Password):    
        params = {
            'Username' : Username,
            'Password' : Password
        }  
        query = """INSERT INTO user (Username, Password)
            values (%(Username)s, %(Password)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)
        
        data = {'DNI': cursor.lastrowid, 'Username': Username, 'Password': Password}
        return data

    def delete_user(self, DNI):    
        params = {'DNI' : DNI}      
        query = """delete from user where DNI = %(DNI)s""" 
        self.mysql_pool.execute(query, params, commit=True) 

        data = {'result': 1}
        return data

#update
##################################################

    def update_user_username(self, Username): 
        params = {'Username' : Username}
        rv = self.mysql_pool.execute("UPDATE user SET", params)

        data = {'result': 1}
        return data


    def update_user_password(self, Password):   
        params = {'Password' : Password}     
        query = """UPDATE from user SET"""
        self.mysql_pool.execute(query, params, commit=True)

        data = {'result': 1}
        return data

#informacion_Usuario
##################################################

    def get_info_user(self, DNI): 
        params = {'DNI' : DNI}
        rv = self.mysql_pool.execute("SELECT * from informacion_Usuario where DNI=%(DNI)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'DNI': result[0], 'Nombre': result[1], 'Apellido_P': result[2], 'Apellido_M': result[3], 'Correo': result[4], 'Direccion': result[5], 'Provincia': result[6], 'Departamento': result[7], 'Codigo_postal': result[8], 'Telefono': result[9]}
            data.append(content)
            content = {}
        return data

    def get_info_users(self):  
        rv = self.mysql_pool.execute("SELECT * from informacion_Usuario")  
        data = []
        content = {}
        for result in rv:
            content = {'DNI': result[0], 'Nombre': result[1], 'Apellido_P': result[2], 'Apellido_M': result[3], 'Correo': result[4], 'Direccion': result[5], 'Provincia': result[6], 'Departamento': result[7], 'Codigo_postal': result[8], 'Telefono': result[9]}
            data.append(content)
            content = {}
        return data

    def add_info_user(self, Nombre, Apellido_P, Apellido_M, Correo, Direccion, Provincia, Departamento, Codigo_postal, Telefono):    
        params = {
            'Nombre' : Nombre,
            'Apellido_P' : Apellido_P,
            'Apellido_M' : Apellido_M,
            'Correo' : Correo,
            'Direccion' : Direccion,
            'Provincia' : Provincia,
            'Departamento' : Departamento,
            'Codigo_postal' : Codigo_postal,
            'Telefono' : Telefono
        }  
        
        query = """INSERT INTO informacion_Usuario (Nombre, Apellido_P, Apellido_M, Correo, Direccion, Provincia, Departamento, Codigo_postal, Telefono)
            values (%(Nombre)s, %(Apellido_P)s, %(Apellido_M)s, %(Correo)s, %(Direccion)s, %(Provincia)s, %(Departamento)s, %(Codigo_postal)s, %(Telefono)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)
        
        data = {'DNI': cursor.lastrowid, 'Nombre': Nombre, 'Apellido_P' : Apellido_P, 'Apellido_M' : Apellido_M, 'Correo' : Correo, 'Direccion' : Direccion, 'Provincia' : Provincia, 'Departamento' : Departamento, 'Codigo_postal' : Codigo_postal, 'Telefono' : Telefono}
        return data

    def delete_info_user(self, DNI):    
        params = {'DNI' : DNI}      
        query = """delete from informacion_Usuario where DNI = %(DNI)s""" 
        self.mysql_pool.execute(query, params, commit=True) 

        data = {'result': 1}
        return data


#Admin
##################################################


    def get_admin(self, ID_Admin): 
        params = {'ID_Admin' : ID_Admin}
        rv = self.mysql_pool.execute("SELECT * from Admin where ID_Admin=%(ID_Admin)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'Username': result[0], 'Password': result[1]}
            data.append(content)
            content = {}
        return data

    def add_admin(self, Username, Password):    
        params = {
            'Username' : Username,
            'Password' : Password
        }  
        query = """INSERT INTO Admin (Username, Password)
            values (%(Username)s, %(Password)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)
        
        data = {'ID_Admin': cursor.lastrowid, 'Username': Username, 'Password': Password}
        return data

    def delete_admin(self, ID_Admin):    
        params = {'ID_Admin' : ID_Admin}      
        query = """delete from Admin where ID_Admin = %(ID_Admin)s""" 
        self.mysql_pool.execute(query, params, commit=True) 

        data = {'result': 1}
        return data


##################################################



###################################################


if __name__ == "__main__":    
    tm = TaskModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    print(tm.delete_task(67))
    print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))