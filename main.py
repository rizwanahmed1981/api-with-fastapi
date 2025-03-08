from fastapi import FastAPI
import random

app = FastAPI()

# we will build two simple get endpoints
# side_hustle
# money_quotes

side_hustles = [
    "Freelance writing",
    "Graphic design",
    "Web development",
    "Tutoring",
    "Dropshipping",
    "Affiliate marketing",
    "Stock photography",
    "Social media management",
    "Print-on-demand store",
    "Blogging",
    "YouTube content creation",
    "Podcasting",
    "Virtual assistant services",
    "Handmade crafts selling",
    "Selling digital products",
    "Online course creation",
    "E-book writing and selling",
    "Remote tech support",
    "App development",
    "Data entry jobs"
]


money_quotes = [
    ("“An investment in knowledge pays the best interest.”", "Benjamin Franklin"),
    ("“The stock market is filled with individuals who know the price of everything, but the value of nothing.”", "Philip Fisher"),
    ("“Do not save what is left after spending, but spend what is left after saving.”", "Warren Buffett"),
    ("“The goal isn’t more money. The goal is living life on your terms.”", "Chris Brogan"),
    ("“Money often costs too much.”", "Ralph Waldo Emerson"),
    ("“Too many people spend money they earned to buy things they don’t want, to impress people that they don’t like.”", "Will Rogers"),
    ("“Wealth consists not in having great possessions, but in having few wants.”", "Epictetus"),
    ("“Formal education will make you a living; self-education will make you a fortune.”", "Jim Rohn"),
    ("“It’s not about having lots of money. It’s knowing how to manage it.”", "Unknown"),
    ("“A wise person should have money in their head, but not in their heart.”", "Jonathan Swift")
]

@app.get('/side_hustles')
def get_side_hustles(apikey: str):
    """Returns a random side hustle idea"""
    if apikey != "rizwan123":
        return {"Error": "Invalid API key"}
    return {"Side Hustle": random.choice(side_hustles)}

@app.get('/money_quotes')
def get_money_qoutes(apikey: str):
    """Returns a random side hustle idea"""
    if apikey != "rizwan123":
        return {"Error": "Invalid API key"}
    return {"Money Qoute": random.choice(money_quotes)}