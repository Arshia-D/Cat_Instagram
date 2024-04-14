import os
import subprocess

def generate_docs(app_name):
    
    base_dir = os.path.join(os.getcwd(), app_name)
    docs_dir = os.path.join(base_dir, 'docs')
    
    # List of components for which to generate documentation
    components = ['models', 'views', 'urls', 'admin', 'tests', 'apps']

    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    for component in components:
        filename = f'{component}.py'
        module_path = os.path.join(app_name, filename).replace('\\', '/')
        
        # Generating the documentation using pydoc
        doc_output = subprocess.run(['pydoc', module_path], capture_output=True, text=True)
        doc_text = doc_output.stdout

        # Saving the documentation to a text file
        with open(os.path.join(docs_dir, f'{component}.txt'), 'w') as doc_file:
            doc_file.write(doc_text)

    print(f'Documentation generated in {docs_dir}')

if __name__ == "__main__":
    generate_docs('Posts')  
