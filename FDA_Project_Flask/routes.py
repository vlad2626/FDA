from FDA_Project_Flask import app, forms
from flask import request, render_template

@app.route('/')
def index():
    return" this is a test please type search after the adress"


@app.route('/search', methods=["GET", "POST"])
def search():
    search_form = forms.SearchByStateForm(request.form)

    if request.method == 'POST':
        """Assign to the following variables the input values by the user"""
        state = request.form['state_input']
        startdate =request.form['startdate_input']
        enddate =request.form['enddate_input']

        """Pass the variables above as arguments to the get_data function 
        and assign the return value to fda_recall"""
        fda_recall = forms.get_data(state,startdate,enddate)

        return render_template('recall_results.html', form=search_form, statename=state, startdate=startdate,
                               enddate=enddate, recall=fda_recall)

    return render_template('recall_search.html', form=search_form)