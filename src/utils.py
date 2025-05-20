from typing import List
import tkinter as tk

def get_lines(text_widget) -> List[str]:
    """
    Retorna lista de linhas não vazias do widget de texto.
    
    Args:
        text_widget: Widget de texto a ser processado
            
    Returns:
        list: Lista de linhas não vazias
    """
    return [line for line in text_widget.get(1.0, tk.END).split('\n') if line.strip()]

def format_items(items: List[str]) -> str:
    """
    Formata os itens do relatório com capitalização e pontuação.
    
    Args:
        items: Lista de itens a serem formatados
            
    Returns:
        str: Texto formatado com bullets e pontuação
    """
    formatted_items = []
    for item in items:
        text = item[2:] if item.startswith('- ') else item
        text = text[0].upper() + text[1:] if text else text
        
        if text and not text.strip()[-1] in '.!?':
            text = text.strip() + '.'
        
        if text.strip():
            formatted_items.append(text)
    
    if not formatted_items:
        return "- Nenhum."
    return "\n".join([f"- {item}" for item in formatted_items])

def generate_report(data: str, squad: str, sprint: str, 
                   progressos: List[str], planos: List[str], 
                   problemas: List[str]) -> str:
    """
    Gera o relatório completo com todos os campos e seções.
    
    Args:
        data: Data do relatório
        squad: Nome do squad
        sprint: Número da sprint
        progressos: Lista de progressos
        planos: Lista de planos
        problemas: Lista de problemas
    
    Returns:
        str: Relatório formatado completo
    """
    return f"""PPP REPORT
DATA: {data}
SQUAD: {squad}
SPRINT(s): {sprint}
===========
PROGRESSOS
{format_items(progressos)}
===========
PLANOS
{format_items(planos)}
===========
PROBLEMAS
{format_items(problemas)}
"""