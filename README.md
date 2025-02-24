# EQ(REX) Decider

## Overview
EQ(REX) Decider is a tool designed to help users make decisions based on a set of predefined criteria. It leverages advanced algorithms to provide the best possible recommendations.

### This provides the following :
- A_REX Decider (acceptance problem for regular expressions)
- EQ_REX Decider (Equivalence problem for regular expressions), keep in mind that EQ_REX is NP
- string generator from the Langauge of a regular expression
- NFA visualiser
- 
 

## Features
- User-friendly interface
- Customizable decision criteria
- Advanced recommendation algorithms
- Real-time decision updates

## Installation
To install EQ(REX) Decider, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Quantum-Object/EQ(REX)-Decider.git
    ```
2. Navigate to the project directory:
    ```bash
    cd EQ(REX)-Decider
    ```


## Usage
To start using EQ(REX) Decider, run the following command:
```bash
python3 main.py
```
**note: we are only using the following operations (\*: Kleene star, |: Union, . : Concatenation (you can ignore it if you want) ).  
example: a\*(a U b).b:= a\*(a|b)b or a\*(a|b)b**.  
-Follow the on-screen instructions to input your decision criteria and receive recommendations.



## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


