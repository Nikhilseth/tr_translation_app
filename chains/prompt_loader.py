def read_prompt_file(filename):
    with open(filename, 'r') as f:
        prompt_template = f.read()
    return prompt_template
