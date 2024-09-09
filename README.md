# CrewAI Travel Itinerary Generator

**CrewAI Travel Itinerary Generator** is an AI-driven application that creates personalized travel itineraries using the CrewAI framework and LMStudio API for local language model operations. This app provides tailored suggestions for destinations, activities, accommodations, and more, offering travelers a smooth and dynamic planning experience.

## Features

- **Personalized Travel Plans**: Generate unique travel itineraries based on user preferences such as budget, interests, and duration.
- **AI-Powered Insights**: Utilizes the CrewAI framework to deliver smart recommendations for must-see attractions, local cuisine, and hidden spots.
- **LMStudio API Integration**: Leverages a locally hosted LMStudio API for language model operations, ensuring fast and private response generation.
- **Real-Time Data**: Get live updates on weather, local events, and other time-sensitive activities.
- **Interactive Adjustments**: Customize itineraries with ease by providing additional inputs or modifying suggestions dynamically.
- **Multi-Language**: Supports multiple languages for a global user base.
- **Offline Access**: Download itineraries for use when traveling without an internet connection.

## Tech Stack

- **Backend**: Python, CrewAI framework
- **AI**: CrewAI agentic framework + LMStudio API running locally for personalized responses
- **APIs**: 
- **Database**: MongoDB for storing user data and itinerary preferences
- **Tools**: DuckduckduckgoSearch

## Prerequisites

- **LMStudio API**: Ensure LMStudio is installed and running locally. Follow the [LMStudio documentation](https://lmstudio.docs) to set up.
- **Python 3.10**

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/crewai-travel-itinerary-generator.git
    cd crewai-travel-itinerary-generator
    ```

2. **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Node.js dependencies**:
    ```bash
    npm install
    ```

4. **Start LMStudio API** (ensure it's running locally at `http://localhost:1234`):
    ```bash
    lmstudio start --host 127.0.0.1 --port 1234
    ```

5. **Set environment variables**:
    Create a `.env` file in the project root with the following contents:
    ```bash
    LMSTUDIO_API_URL=http://localhost:1234/v1
    CREWAI_MODEL=local-model
    ```

6. **Run the app**:
    - **Backend**:
      ```bash
      python app.py
      ```
    - **Frontend**:
      ```bash
      
      ```

7. **Access the application**:
   Open your browser and go to `http://localhost:3000`. this part is not implemented yet.

## Usage

1. **Input Preferences**: Fill out your travel details such as destination, budget, preferred activities, and travel dates.
2. **Generate Itinerary**: Click "Generate Itinerary" to create a custom travel plan using AI.
3. **Modify Suggestions**: Adjust the recommendations in real-time based on new input or preferences.
4. **Save & Share**: Save the final itinerary as a PDF or export it in other formats to share with friends or family.

## Contributing

We welcome all contributions to improve the project. To contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add your feature"
    ```
4. Push to your branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please reach out at support@crewai.com.
