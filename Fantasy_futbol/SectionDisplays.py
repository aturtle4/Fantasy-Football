from Scraper.NewsScraper import NewsScraper
import tkinter as tk 
from tkinter import ttk

def open_news(news_link):
    import webbrowser
    webbrowser.open(news_link)



def display_market_values_section(section_frame):
    #lets do this now
    #lets get current market values
    
    
    pass

def display_leagues_section(section_frame):
    pass

def display_match_details_section(section_frame):
    pass
def display_fantasy_football_section(section_frame):
    pass
def display_news_section(section_frame):
    n = NewsScraper()
    n.scrape_news()
    d = n.get_news()
    
    canvas = tk.Canvas(section_frame,width=860,height=600, bg='black',borderwidth = 10)
    canvas.grid(row=0, column=0, sticky='nsew')
    
    scrollbar = ttk.Scrollbar(section_frame, orient='vertical', command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    
    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas, bg='black')
    canvas.create_window((300, 300), window=frame, anchor='nw')

    for headline, link in d.items():
        t = headline.replace("&apos;","'")
        t =t.replace("&amp;","&")
        button = tk.Button(frame, text=t, bg='black', fg='white', font=('Helvetica', 12), relief='flat', width=100, command=lambda l=link: open_news(l))
        button.pack(pady=5)

    frame.update_idletasks()
    
    # Update the canvas to the size of the frame
    canvas.config(scrollregion=canvas.bbox('all'))
    canvas.xview_moveto(1.0)
