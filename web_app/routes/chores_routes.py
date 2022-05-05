
from flask import Blueprint, request, render_template, redirect, flash

from app.chores_function import chores

from app.email import send_email

import random

chores_routes = Blueprint("chores_routes", __name__)

@chores_routes.route("/chores/assignments")
def chores_assignments():
    print("CHORE ASSIGNMENTS...")
    return render_template("chores_assignments.html")

@chores_routes.route("/chores/results", methods = ["GET", "POST"])
def chores_results():

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    members = request_data.get("members")
    chores = request_data.get("chores")
    emails = request_data.get("emails")
    

    members = list(members.split(","))
    chores = list(chores.split(","))
    emails = list(emails.split(","))

    data = dict()

    data = {"members": [], "chores": [], "emails":[]}

    data["members"] = members
    data["chores"] = chores
    data["emails"] = emails

    assignments = dict()

    for member in data["members"]:
        assignments[member] = []

    for member in assignments:
        assignments[member] = dict()
        assignments[member]["tasks"] = []
        assignments[member]["email"] = []
    
    for email in data["emails"]:
        assignments[member]["email"] = email

    chores = data["chores"]

    while len(chores) > 0:
        for member in assignments:
            task = random.choice(chores)
            chores.remove(task)
            assignments[member]["tasks"].append(task)

    assigned_chores = []

    for member in assignments:
        tasks = assignments[member]["tasks"]
        chores = ' & '.join(', '.join(tasks).rsplit(', ', 1))
        y = " | "
        x = member + y + chores
        assigned_chores.append(x)

    example_subject = "Weekly Chore Assignment"

    for member in assignments:
        tasks = assignments[member]["tasks"]

        chores = ' & '.join(', '.join(tasks).rsplit(', ', 1))

        example_recipient_address = assignments[member]["email"]

        example_html = f"""
            <h3>These are your following chores for the week</h3>

            <h4>My Chores:</h4>
            <ul>
                <p> - {chores} </p>   
            </ul>
            """

        send_email(example_subject, example_html, example_recipient_address)

    flash("Here are the chore assignments:")
    return render_template("chores_results.html", assignments = assigned_chores)