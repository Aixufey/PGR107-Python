graph TD
A[Game] --> B[login]
B -->|existing user|C[show_menu]
B -->|new user|D[create_user]
D --> C
C -->|1|E[show_users]
C -->|2|F[show_high_scores]
C -->|3|G[handle_game]
G --> H[prepare_game]
H --> I[handle_guess]
I -->|correct guess|J[update_user_csv]
J --> C
I -->|out of tries|K[handle_game]
K --> H
C -->|4|L[Exit]