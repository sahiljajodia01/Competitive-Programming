// This is not complete. The logic for finding 2nd max is left for now.


#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;


    while(t--) {
        map<string, int> m1, m2;

        for(int i = 0; i < 12; i++) {
            string team1, team2;
            int goal1, goal2;
            string temp;

            cin >> team1 >> goal1 >> temp >> goal2 >> team2;

            if(goal1 > goal2) {
                if(m1.find(team1) == m1.end()) {
                    m1[team1] = 3;
                }
                else {
                    m1[team1] += 3;
                }
            }
            else if(goal1 < goal2) {
                if(m1.find(team2) == m1.end()) {
                    m1[team2] = 3;
                }
                else {
                    m1[team2] += 3;
                }
            }
            else {
                if((m1.find(team2) == m1.end()) && (m1.find(team1) == m1.end())) {
                    m1[team2] = 1;
                    m1[team1] = 1;
                }
                else if((m1.find(team2) == m1.end()) && (m1.find(team1) != m1.end())) {
                    m1[team2] = 1;
                    m1[team1] += 1;
                }
                else if((m1.find(team2) != m1.end()) && (m1.find(team1) == m1.end())) {
                    m1[team2] += 1;
                    m1[team1] = 1;
                }
                else {
                    m1[team2] += 1;
                    m1[team1] += 1;
                }
            }



            if((m1.find(team2) == m1.end()) && (m1.find(team1) == m1.end())) {
                m2[team1] = (goal1 - goal2);
                m2[team2] = (goal2 - goal1);
            }
            else if((m1.find(team2) == m1.end()) && (m1.find(team1) != m1.end())) {
                m2[team1] += (goal1 - goal2);
                m2[team2] = (goal2 - goal1);
            }
            else if((m1.find(team2) != m1.end()) && (m1.find(team1) == m1.end())) {
                m2[team1] = (goal1 - goal2);
                m2[team2] += (goal2 - goal1);
            }
            else {
                m2[team1] += (goal1 - goal2);
                m2[team2] += (goal2 - goal1);
            }


        }


        int max = INT_MIN;
        int second_num = INT_MIN;
        for(map<string, int>::iterator it = m1.begin(); it != m1.end(); it++) {
            int second = it->second;

            if(second > max) {
                second_num = max;
                max = second;
            }
        }

        vector<string> v_first, v_second;
        for(map<string, int>::iterator it = m1.begin(); it != m1.end(); it++) {
            int second = it->second;
            string first = it->first;

            if(second == max) {
                v_first.push_back(first);
            }
            else if(second == second_num) {
                v_second.push_back(first);
            }
        }

        max = INT_MIN;
        second_num = INT_MIN;
        string max_s = "", second_s = "";
        if(v_first.size() > 1) {
            int max_goal = 0;
            for(int i = 0; i < v_first.size(); i++) {
                for(map<string, int>::iterator it = m2.begin(); it != m2.end(); it++) {
                    string first = it->first;
                    int second = it->second;

                    if(first == v_first[i] && second > max) {
                        second_num = max;
                        second_s = max_s;
                        max = second;
                        max_s = first;
                        break;
                    }
                }
            }


            // for(int i = 0; i < v_second.size(); i++) {
            //     for(map<string, int>::iterator it = m2.begin(); it != m2.end(); it++) {
            //         string first = it->first;
            //         int second = it->second;

            //         if(first == v_second[i] && second > second_num) {
            //             second_num = second;
            //             second_s = first;
            //             break;
            //         }
            //     }
            // }

            cout << max_s << " " << second_s << "\n";
            
        }
        else {
            max = INT_MIN;
            max_s = "";

            if(v_second.size() > 1) {
                for(int i = 0; i < v_second.size(); i++) {
                    for(map<string, int>::iterator it = m2.begin(); it != m2.end(); it++) {
                        string first = it->first;
                        int second = it->second;

                        if(first == v_first[i] && second > max) {
                            max = second;
                            max_s = first;
                            break;
                        }
                    }
                }

                cout << v_first[0] << " " << max_s << "\n";
            }
            else {
                cout << v_first[0] << " " << v_second[0] << "\n";
            }

        }
    }
}