# password-saver

COMMAND LIST:
- login user_name password
- logout
- mkuser user_name password
- rmuser user_name
- mktag tag_name
- mksub tag_name sub_tag_name
- uvpw tag_name sub_tag_name username password

Note: to start use the following command -> python pw.py start
---
Terminology:
- Tag: A category of passwords to save.
- Sub-Tag: A sub-category of passwords to save.

---
Directory information:
- "users" directory stores folder that belong to each user.
- "uv" directory stores credentials in a file in it.

{users/<user_folder>/<tag_folder>/<sub-tag-file>}
