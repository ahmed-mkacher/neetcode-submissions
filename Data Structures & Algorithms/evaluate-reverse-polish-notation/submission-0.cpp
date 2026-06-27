class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> v;
        int r = 0;

        for (string c : tokens) {
            if (c == "+") { 
                r = v.top();
                v.pop();
                r += v.top();
                v.pop();
                v.push(r);
            } else if (c == "*") {
                r = v.top();
                v.pop();
                r *= v.top();
                v.pop();
                v.push(r);
            } else if (c == "/") {
                r = v.top();
                v.pop();
                r = v.top() / r;
                v.pop();
                v.push(r);
            } else if (c == "-") {
                r = v.top();
                v.pop();
                r = v.top() - r;
                v.pop();
                v.push(r);
            }
            else {
                v.push(stoi(c));
            }
        }

        return v.top();
    }
};
