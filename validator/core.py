# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import json
import os

class JsonValidator:
    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Parse it
            # Python's json.load is strict by default (no comments, no trailing commas)
            json.loads(content)
            
        except json.JSONDecodeError as e:
            issues.append({
                'line': e.lineno,
                'col': e.colno,
                'file': filepath,
                'msg': e.msg
            })
        except Exception as e:
            issues.append({
                'line': 0,
                'col': 0,
                'file': filepath,
                'msg': str(e)
            })
            
        return issues

    @staticmethod
    def scan_directory(directory):
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                if file.endswith('.json'):
                    path = os.path.join(root, file)
                    issues = JsonValidator.scan_file(path)
                    all_issues.extend(issues)
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
