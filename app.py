from flask import Flask, render_template, request
from db_connector import fetch_data
from chroma_module import add_to_vector_store, search_similar
from langchain_module import ask_gemini

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_query = request.form["query"]
        db_result = fetch_data(user_query)
        
        # Add fetched data to Chroma Vector DB
        if db_result:
            docs = [str(item) for item in db_result]
            add_to_vector_store("example_collection", docs)

        # Query Chroma DB for similar items
        vector_results = search_similar("example_collection", user_query)

        # Generate insights using Gemini
        insight = ask_gemini(f"Summarize this database query result: {db_result}")

        result = {
            "db_data": db_result,
            "vector_search": vector_results,
            "gemini_summary": insight
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)