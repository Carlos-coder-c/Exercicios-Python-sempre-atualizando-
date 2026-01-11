def lidar_eventos(payload: dict) -> None:
  match payload:
    case {"type": "user", "action": "created", "id": user_id}:
     create_user(user_id)
      
    case {"type": "user", "action": "deleted", "id": user_id}:
      delete_user(user_id)
    
    case   {"type": "order", "status": "paid", "amount": amount}:
     process_payment(amount)
    
    case _:
      raise ValueError('Payload Invalido')
       
     


