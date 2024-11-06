def is_safe(board, row, col, N):
    # Cek kolom di atas
    for i in range(row):
        if board[i] == col:
            return False

    # Cek diagonal utama di atas (dari kiri-atas ke kanan-bawah)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Cek diagonal sekunder di atas (dari kanan-atas ke kiri-bawah)
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if i >= 0 and j < N and board[i] == j:
            return False

    return True

def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        # Jika semua ratu berhasil ditempatkan, tambahkan solusi ke daftar
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col  # Tempatkan ratu
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row] = -1  # Hapus ratu (backtrack)

def solve_n_queens(N):
    board = [-1] * N  # Inisialisasi papan dengan -1 (tidak ada ratu)
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

def print_solutions(solutions, N):
    for solution in solutions:
        for row in solution:
            line = ""
            for col in range(N):
                if col == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n" + "-" * (2 * N - 1) + "\n")

# Menjalankan program N-Queen untuk N = 8
N = 8
solutions = solve_n_queens(N)
print(f"Jumlah solusi untuk {N}-Queen: {len(solutions)}")
print("Contoh solusi:")
print_solutions(solutions[:5], N)  # Menampilkan 5 solusi pertama sebagai contoh
