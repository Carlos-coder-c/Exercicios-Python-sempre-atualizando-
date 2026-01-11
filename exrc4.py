#match e case 

def lidar_status(status: int) -> str:
 match status:
   case 200:
     'Ok'
   case 201:
     'Criado'
   case 400:
     'Requisição invalida' 
   case 401 | 403:
     'Não Autorizado'
   case _:
     'Erro desconhecido'
     