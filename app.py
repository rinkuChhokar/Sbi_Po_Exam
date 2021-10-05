from flask import Flask,render_template


app=Flask(__name__,template_folder='templates')
app.secret_key = 'super secret key'

@app.route("/")

def sbi():
	return render_template("SBI_PO_EXAM.html")


if __name__ == "__main__":
    app.run(debug=False)   

