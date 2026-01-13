from datetime import datetime
from langchain.tools import tool

@tool
def get_actual_date_tool() -> datetime.date:
    """
    Returns the actual date.
    
    :return: actual date
    :rtype: datetime.datetime
    """
    return datetime.now()

@tool
def get_categories() -> list:
    """
    Returns a list with all the available categories.
    
    :return: list with strings of spend categories
    :rtype: list
    """
    categorias_gastos = [
        "ALIMENTACIÓN",
        "VIVIENDA",
        "TRANSPORTE",
        "SERVICIOS",
        "ENTRETENIMIENTO"
    ]
    return categorias_gastos

@tool
def insert_spend(amount: float, category: str) -> str:
    """
    Docstring for insert_spend
    
    :param amount: Money amount
    :type amount: float
    :param category: Spend category.
    :type category: str
    :return: String confirmation of the inserted spend.
    :rtype: str
    """
    return f"Tu gasto de {amount} en la categoria {category} ha sido registrado correctamente."

finance_tools = [get_actual_date_tool, insert_spend, get_categories]