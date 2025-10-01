from django.db import connection

def executar_sp_depositar(correntista_id: int, valor_deposito: float):
    sql_command = "EXEC [dbo].[spDepositar] %s, %s"
    params = [correntista_id, valor_deposito]
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_command, params)
            connection.commit()
 
            return True
            
    except Exception as e:
        connection.rollback()
        raise ValueError(f"Erro ao depositar na conta {correntista_id}: {e}")
    
def executar_sp_pagar(correntista_id: int, valor_operacao: float, descricao: str):
    sql_command = "EXEC [dbo].[spPagar] %s, %s, %s"
    params = [correntista_id, valor_operacao, descricao]
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_command, params)
            connection.commit()
 
            return True
            
    except Exception as e:
        connection.rollback()
        raise ValueError(f"Erro ao processar pagamento na conta {correntista_id}: {e}")
    

def executar_sp_transferir(correntista_id: int, valor_operacao: float, CorrentistaBeneficiari_id: int):
    sql_command = "EXEC [dbo].[spTransferir] %s, %s, %s"
    params = [correntista_id, valor_operacao, CorrentistaBeneficiari_id]
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_command, params)
            connection.commit()
 
            return True
            
    except Exception as e:
        connection.rollback()
        raise ValueError(f"Erro ao processar transferência na conta {correntista_id}: {e}")
    

def executar_sp_sacar(correntista_id: int, valor_saque: float):
    sql_command = "EXEC [dbo].[spSacar] %s, %s"
    params = [correntista_id, valor_saque]
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_command, params)
            connection.commit()
 
            return True
            
    except Exception as e:
        connection.rollback()
        raise ValueError(f"Erro ao sacar da conta {correntista_id}: {e}")
    
def executar_vw_extrato(correntista_id: int):
    sql_command = "SELECT * FROM [dbo].[vwExtrato] WHERE CorrentistaID = %s"
    params = [correntista_id]
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_command, params)
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
 
            return results
            
    except Exception as e:
        raise ValueError(f"Erro ao recuperar extrato para a conta {correntista_id}: {e}")
    