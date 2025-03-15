from flask import Flask, jsonify, abort
from flask_cors import CORS
import json
import os

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

# Map of channel IDs to result files
CHANNEL_MAPPING = {
    'test': 'test_results.json',
    'mkbhd': 'mkbhd_ytdlp_1video_with_quotes.json'
}

@app.route('/api/results', methods=['GET'])
def get_all_results():
    """Legacy endpoint that returns the test results"""
    with open('test_results.json', 'r') as file:
        results = json.load(file)
    return jsonify(results)

@app.route('/api/recommendations/<channel_id>', methods=['GET'])
def get_channel_recommendations(channel_id):
    """Get recommendation results for a specific channel ID"""
    # Check if channel exists in our mapping
    if channel_id not in CHANNEL_MAPPING:
        abort(404, description=f"Channel '{channel_id}' not found")
    
    # Get the associated file
    filename = CHANNEL_MAPPING[channel_id]
    
    # Check if file exists
    if not os.path.exists(filename):
        abort(404, description=f"Results for channel '{channel_id}' not available")
    
    # Read and return the results
    with open(filename, 'r') as file:
        results = json.load(file)
    return jsonify(results)

# Add a root endpoint to list available channels
@app.route('/', methods=['GET'])
def list_channels():
    """List all available channels"""
    channels = list(CHANNEL_MAPPING.keys())
    return jsonify({
        'available_channels': channels,
        'example_usage': 'http://example.com/api/recommendations/mkbhd'
    })

if __name__ == '__main__':
    # Get port from environment variable for Railway or use 5001 as fallback
    port = int(os.environ.get("PORT", 5001))
    print(f"Starting Flask API server with CORS enabled on port {port}...")
    print("Available endpoints:")
    print(f"  - /api/results (Legacy endpoint)")
    print(f"  - /api/recommendations/<channel_id>")
    print(f"Available channels: {list(CHANNEL_MAPPING.keys())}")
    app.run(debug=True, host='0.0.0.0', port=port)