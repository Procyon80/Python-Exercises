from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BMI Calculator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 450px;
            width: 100%;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 32px;
        }
        .input-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: 600;
            font-size: 14px;
        }
        input {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        input:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
            margin-top: 10px;
        }
        button:hover {
            transform: translateY(-2px);
        }
        button:active {
            transform: translateY(0);
        }
        .result {
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            display: none;
        }
        .result.show {
            display: block;
        }
        .result h2 {
            font-size: 24px;
            margin-bottom: 10px;
        }
        .result p {
            font-size: 18px;
            margin: 5px 0;
        }
        .underweight {
            background: #e3f2fd;
            border: 2px solid #2196f3;
            color: #1976d2;
        }
        .normal {
            background: #e8f5e9;
            border: 2px solid #4caf50;
            color: #388e3c;
        }
        .overweight {
            background: #fff3e0;
            border: 2px solid #ff9800;
            color: #f57c00;
        }
        .obese {
            background: #ffebee;
            border: 2px solid #f44336;
            color: #d32f2f;
        }
        .info {
            margin-top: 20px;
            padding: 15px;
            background: #f5f5f5;
            border-radius: 8px;
            font-size: 12px;
            color: #666;
        }
        .info h3 {
            margin-bottom: 8px;
            color: #333;
            font-size: 14px;
        }
        .error {
            color: #f44336;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏋️ BMI Calculator</h1>
        <form id="bmiForm">
            <div class="input-group">
                <label for="weight">Weight (kg)</label>
                <input type="number" id="weight" step="0.1" min="0" required>
                <div class="error" id="weightError"></div>
            </div>
            <div class="input-group">
                <label for="height">Height (m)</label>
                <input type="number" id="height" step="0.01" min="0" required>
                <div class="error" id="heightError"></div>
            </div>
            <button type="submit">Calculate BMI</button>
        </form>
        <div class="result" id="result"></div>
        <div class="info">
            <h3>BMI Categories:</h3>
            <p><strong>Underweight:</strong> BMI < 18.5</p>
            <p><strong>Normal weight:</strong> BMI 18.5 - 24.9</p>
            <p><strong>Overweight:</strong> BMI 25 - 29.9</p>
            <p><strong>Obese:</strong> BMI ≥ 30</p>
        </div>
    </div>
    <script>
        document.getElementById('bmiForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const weight = parseFloat(document.getElementById('weight').value);
            const height = parseFloat(document.getElementById('height').value);
            
            if (weight <= 0 || height <= 0) {
                alert('Please enter positive values!');
                return;
            }
            
            const bmi = weight / (height * height);
            let category, categoryClass;
            
            if (bmi < 18.5) {
                category = 'Underweight';
                categoryClass = 'underweight';
            } else if (bmi < 25) {
                category = 'Normal weight';
                categoryClass = 'normal';
            } else if (bmi < 30) {
                category = 'Overweight';
                categoryClass = 'overweight';
            } else {
                category = 'Obese';
                categoryClass = 'obese';
            }
            
            const resultDiv = document.getElementById('result');
            resultDiv.className = 'result show ' + categoryClass;
            resultDiv.innerHTML = `
                <h2>Your BMI: ${bmi.toFixed(2)}</h2>
                <p><strong>Category: ${category}</strong></p>
            `;
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("🚀 BMI Calculator is running!")
    print("📱 Open your browser and go to: http://127.0.0.1:5000")
    print("⏹️  Press CTRL+C to stop the server")
    app.run(debug=True, port=5000)