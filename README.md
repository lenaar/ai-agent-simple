# AI Agent Simple

A Python-based AI agent that can calculate celestial body masses and perform scientific calculations.

## Features

- Calculate combined masses of multiple planets
- Handle scientific notation (e.g., 1.898e24)
- Interactive command-line interface
- Comprehensive test suite

## Installation

```bash
# Clone the repository
git clone https://github.com/lenaar/ai-agent-simple.git
cd ai-agent-simple

# Install dependencies (if any)
pip install pytest
```

## Usage

Run the interactive agent:

```bash
python main.py
```

You'll be prompted to:
1. Enter max turns (5-15)
2. Enter your question about planet masses

Example questions:
- What is the combined mass of Jupiter and Saturn?
- What is the combined mass of Earth, Mars, and Jupiter?

## Testing

Run the test suite:

```bash
python -m pytest tests/ -v
```

## Implementation Details

- `simple_agent.py`: Core agent implementation
- `simple_agent_tools.py`: Tools for calculations and planet mass lookup
- `simple_agent_query.py`: Query processing and skill execution
- `simple_agent_prompt.py`: System prompt and examples

### Available Planets

- Earth (5.972e24 kg)
- Mars (6.4171e24 kg)
- Jupiter (1.898e24 kg)
- Saturn (5.688e24 kg)

## Recent Updates

- Added support for calculating masses of any number of planets
- Improved scientific notation handling
- Made interface interactive with user input
- Added comprehensive test coverage
- Enhanced error handling for unknown planets