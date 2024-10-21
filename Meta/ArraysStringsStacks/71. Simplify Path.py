# https://leetcode.com/problems/simplify-path/

'''
TELL WHY DO YOU WANT TO USE A STACK?

"/a/b/c/././../../" -> use stack to keep track of file/directory names
'''
class Solution:
    # TC - O(N) | SC - O(N)
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split("/"):
            if part == "..":
                if stack: stack.pop()
            elif part == "." or not part:
                continue
            else:
                stack.append(part)

        return "/" + "/".join(stack)


# GOING CHAR BY CHAR (USE THIS IF THE INTERVIEWER SAYS NOT TO USE .split())
# TC - O(N) | SC - O(N)
class Solution1:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path += "/" # to handle case "a/b/c./d/.."
        cur = ""
        
        for c in path:
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)


'''
META ALTERNATE QUESTION - https://leetcode.com/discuss/interview-question/553454/facebook-phone-change-working-directory

Given current directory and change directory path, return final path.

For Example:

Curent                 Change            Output

/                    /facebook           /facebook
/facebook/anin       ../abc/def          /facebook/abc/def
/facebook/instagram   ../../../../.      /

TC - O(N)
SC - O(N)
'''
def change_path(current: str, changed: str) -> str:
    # Linux will also take you to your home directory (aka ~) 
    if not changed:
        return current

    # handle absolute path
    if changed[0] == "/":
        current = ""

    path = []
    for segment in (current + "/" + changed).split("/"):
        if segment == ".": continue
        
        if segment == "..":
            if path:
                path.pop()
        elif segment:
            path.append(segment)

    return "/" + "/".join(path)

print(change_path("/", "a")) # /a
print(change_path("/a", "/b")) # /b
print(change_path("/lol", "../../../../..")) # /
print(change_path("/foo", "bar/../baz/./x")) # /foo/baz/x
print(change_path("/x", "/p/../q")) # /q

print(change_path("/a/b", ".")) # /a/b
print(change_path("/a/b", "..")) # /a
print(change_path("/a/b", "/d/e")) # /d/e
print(change_path("/a/b", "c")) # /a/b/c
print(change_path("/a/b", "c/./d")) # /a/b/c/d