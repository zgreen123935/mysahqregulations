# Mysa HQ Energy Regulations Database Crew

This CrewAI-powered project helps Mysa HQ maintain a comprehensive database of energy regulations, HVAC systems, lighting standards, and safety requirements for commercial properties in North America.

## Overview

The crew consists of three specialized AI agents:

1. **Energy Regulations Researcher**: Gathers and analyzes regulations, standards, and best practices
2. **Database Manager**: Organizes and structures the collected data
3. **Quality Assurance Specialist**: Ensures data accuracy and consistency

## Features

- Comprehensive research of energy regulations and standards
- Structured database organization for easy access
- Quality assurance protocols for data validation
- Focus on HVAC systems, lighting standards, and safety regulations
- Regional coverage for North America

## Requirements

- Python 3.10 or higher
- OpenAI API key
- Serper API key (for web search capabilities)

## Installation

```bash
# Clone the repository
git clone [your-repo-url]
cd [your-repo-name]

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.\.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -e .
```

## Configuration

Set up your API keys:

```bash
export OPENAI_API_KEY='your-api-key-here'
export SERPER_API_KEY='your-serper-api-key-here'
```

## Usage

Run the crew:

```bash
run_crew
```

## Output

The crew will generate:
1. Research findings on energy regulations
2. Structured database of regulations and standards
3. Quality assurance reports

## License

[Your chosen license]
