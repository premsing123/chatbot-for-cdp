from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Documentation links and responses for each platform
documentation = {
    "Segment": {
        "setup_source": """
            To set up a new source in Segment:
            1. Go to the Segment platform.
            2. Navigate to the 'Sources' section.
            3. Click 'Add Source'.
            4. Select the appropriate source type (e.g., website, app).
            5. Follow the setup instructions specific to the selected source.
            For more information, check the full documentation here: https://segment.com/docs/?ref=nav.
        """,
        "integrate_salesforce": """
            To integrate Segment with Salesforce:
            1. In Segment, create a new destination for Salesforce.
            2. Provide Salesforce credentials and configure the sync settings.
            3. Map the necessary event data to Salesforce fields.
            For further details, see the Segment Salesforce integration guide here: https://segment.com/docs/?ref=nav.
        """,
        "general": """
            Segment helps you collect, clean, and control your customer data.
            It provides tools for data integration, customer journey analytics, and personalizing user experiences.
            For more information, refer to the full documentation: https://segment.com/docs/?ref=nav.
        """
    },
    "mParticle": {
        "general": """
            mParticle helps you integrate and orchestrate customer data from any source.
            For detailed integration steps, refer to: https://docs.mparticle.com/.
            It allows real-time synchronization and user privacy management.
        """
    },
    "Lytics": {
        "general": """
            Lytics helps in building real-time profiles and targeting customer groups.
            Learn more in the documentation: https://docs.lytics.com/.
            It leverages machine learning to build predictive models and integrates with marketing tools.
        """
    },
    "Zeotap": {
        "general": """
            Zeotap enables secure unification and activation of customer data.
            Explore the full documentation here: https://docs.zeotap.com/home/en-us/.
            Zeotap integrates with CRMs and offers deep analytics for customer segmentation.
        """
    }
}

# Function to generate a detailed response based on user input
def generate_response(user_input):
    user_input = user_input.lower().strip()

    # Check if the question is about a specific platform
    if "segment" in user_input:
        if "setup a new source" in user_input:
            return documentation["Segment"]["setup_source"]
        elif "integrate with salesforce" in user_input:
            return documentation["Segment"]["integrate_salesforce"]
        else:
            return documentation["Segment"]["general"]
    elif "mparticle" in user_input:
        return documentation["mParticle"]["general"]
    elif "lytics" in user_input:
        return documentation["Lytics"]["general"]
    elif "zeotap" in user_input:
        return documentation["Zeotap"]["general"]
    else:
        return "Please ask a specific question related to Segment, mParticle, Lytics, or Zeotap."

@app.route('/')
def home():
    return render_template('chat.html')  # Ensure chat.html exists in a 'templates' folder

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('user_input', '')
    if not user_input.strip():
        return jsonify({'response': "Please provide a valid question."})
    
    response = generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
