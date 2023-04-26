# StoryGen
Python a gyakorlatban beadandó, 2023 tavasz

## Pylint eredmény (pylint StoryGen/*.py):
<code>Your code has been rated at 6.88/10</code>

## Flake8 eredmény (flake8 .):
<code>.\StoryGen\app.py:3:1: F403 'from home_frame import *' used; unable to detect undefined names
.\StoryGen\app.py:4:1: F403 'from previous_generations_frame import *' used; unable to detect undefined names
.\StoryGen\app.py:5:1: F403 'from key_frame import *' used; unable to detect undefined names
.\StoryGen\app.py:6:1: F403 'from navigation_frame import *' used; unable to detect undefined names
.\StoryGen\app.py:23:27: F405 'HomeFrame' may be undefined, or defined from star imports: home_frame, key_frame, navigation_frame, previous_generations_frame
.\StoryGen\app.py:28:43: F405 'PreviousGenerationsFrame' may be undefined, or defined from star imports: home_frame, key_frame, navigation_frame, previous_generations_frame
.\StoryGen\app.py:33:26: F405 'KeyFrame' may be undefined, or defined from star imports: home_frame, key_frame, navigation_frame, previous_generations_frame
.\StoryGen\app.py:33:80: E501 line too long (87 > 79 characters)
.\StoryGen\app.py:36:33: F405 'NavigationFrame' may be undefined, or defined from star imports: home_frame, key_frame, navigation_frame, previous_generations_frame
.\StoryGen\home_frame.py:2:1: F403 'from openai_api import *' used; unable to detect undefined names
.\StoryGen\home_frame.py:33:12: F405 'get_api_key' may be undefined, or defined from star imports: openai_api
.\StoryGen\home_frame.py:36:80: E501 line too long (87 > 79 characters)
.\StoryGen\home_frame.py:56:80: E501 line too long (82 > 79 characters)
.\StoryGen\home_frame.py:88:20: F405 'get_response' may be undefined, or defined from star imports: openai_api
.\StoryGen\home_frame.py:96:80: E501 line too long (88 > 79 characters)
.\StoryGen\home_frame.py:133:80: E501 line too long (81 > 79 characters)
.\StoryGen\home_frame.py:142:80: E501 line too long (80 > 79 characters)
.\StoryGen\home_frame.py:156:80: E501 line too long (88 > 79 characters)
.\StoryGen\home_frame.py:163:80: E501 line too long (111 > 79 characters)
.\StoryGen\home_frame.py:177:80: E501 line too long (80 > 79 characters)
.\StoryGen\home_frame.py:193:80: E501 line too long (81 > 79 characters)
.\StoryGen\home_frame.py:195:80: E501 line too long (84 > 79 characters)
.\StoryGen\home_frame.py:227:80: E501 line too long (113 > 79 characters)
.\StoryGen\home_frame.py:234:80: E501 line too long (89 > 79 characters)
.\StoryGen\home_frame.py:262:80: E501 line too long (85 > 79 characters)
.\StoryGen\home_frame.py:339:22: F405 'generate_image' may be undefined, or defined from star imports: openai_api
.\StoryGen\key_frame.py:54:80: E501 line too long (80 > 79 characters)
.\StoryGen\navigation_frame.py:9:80: E501 line too long (81 > 79 characters)
.\StoryGen\navigation_frame.py:32:80: E501 line too long (86 > 79 characters)
.\StoryGen\navigation_frame.py:33:80: E501 line too long (84 > 79 characters)
.\StoryGen\navigation_frame.py:101:80: E501 line too long (85 > 79 characters)
.\StoryGen\navigation_frame.py:145:80: E501 line too long (80 > 79 characters)
.\StoryGen\openai_api.py:23:80: E501 line too long (88 > 79 characters)
.\StoryGen\openai_api.py:50:80: E501 line too long (88 > 79 characters)
.\StoryGen\openai_api.py:53:80: E501 line too long (84 > 79 characters)
.\StoryGen\previous_generations_frame.py:28:80: E501 line too long (81 > 79 characters)
.\StoryGen\previous_generations_frame.py:87:80: E501 line too long (83 > 79 characters)
.\StoryGen\previous_generations_frame.py:95:80: E501 line too long (83 > 79 characters)
.\StoryGen\previous_generations_frame.py:96:80: E501 line too long (82 > 79 characters)
.\StoryGen\test.py:24:13: F841 local variable 'response' is assigned to but never used
.\StoryGen\test.py:30:80: E501 line too long (83 > 79 characters)
.\StoryGen\test.py:44:80: E501 line too long (88 > 79 characters)</code>