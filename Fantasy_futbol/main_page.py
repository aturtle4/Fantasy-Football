import tkinter as tk
from tkinter import ttk
from Scraper.NewsScraper import NewsScraper
import SectionDisplays

def main():
    root = tk.Tk()
    root.geometry('900x600')
    root.resizable(False, False)
    root.title('Fantasy Football')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TNotebook', background='black', borderwidth=0)
    style.configure('TNotebook.Tab', padding=(10, 4), relief='flat', font=('Helvetica', 12), background='black', foreground='white')
    style.map('TNotebook.Tab', background=[('selected', 'gray25')])

    notebook = ttk.Notebook(root)
    notebook.grid(row=0, column=0, sticky='nsew')
    
    sections = ["News", "Match Details", "Market Values", "Fantasy Football", "Leagues"]

    for section in sections:
        tab = tk.Frame(notebook, bg='black')
        notebook.add(tab, text=section)

        section_frame = tk.Frame(tab, bg='black')
        section_frame.grid(row=0, column=0, sticky='nsew')
        
        # Set the weight of the row and column to expand fully
        tab.grid_rowconfigure(0, weight=1)
        tab.grid_columnconfigure(0, weight=1)
        
        if section == "News":
            SectionDisplays.display_news_section(section_frame)
        if section == "Match Details":
            SectionDisplays.display_match_details_section(section_frame)
        if section == "Market Values":
            SectionDisplays.display_market_values_section(section_frame)
        if section == "Fantasy Football":
            SectionDisplays.display_fantasy_football_section(section_frame)
        if section == "Leagues":
            SectionDisplays.display_leagues_section(section_frame)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()

if __name__ == '__main__':
    main()
