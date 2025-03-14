import numpy as np


def tao_ma_tran(n, m):
    return np.random.randint(-100, 101, size=(n, m))


def dinh_thuc(ma_tran):
    if ma_tran.shape[0] == ma_tran.shape[1]:
        return np.linalg.det(ma_tran)
    else:
        return "Không thể tính định thức vì ma trận không vuông."


def nghich_dao(ma_tran):
    if ma_tran.shape[0] == ma_tran.shape[1]:
        try:
            return np.linalg.inv(ma_tran)
        except np.linalg.LinAlgError:
            return "Ma trận không có nghịch đảo."
    else:
        return "Không thể tính ma trận nghịch đảo vì ma trận không vuông."


def sap_xep_hang(ma_tran):
    return np.sort(ma_tran, axis=1)


def sap_xep_cot(ma_tran):
    return np.sort(ma_tran, axis=0)


def sap_xep_theo_trung_binh_hang(ma_tran):
    return ma_tran[np.argsort(np.mean(ma_tran, axis=1))]


def thay_doi_phan_tu(ma_tran, hang, cot, gia_tri):
    if 0 <= hang < ma_tran.shape[0] and 0 <= cot < ma_tran.shape[1]:
        ma_tran[hang, cot] = gia_tri
        return ma_tran
    else:
        return "Lỗi: Chỉ mục dòng hoặc cột vượt quá kích thước ma trận!"


def thay_doi_cot(ma_tran, cot):
    ma_tran[:, cot] += 2
    return ma_tran


def cong_vector(ma_tran):
    vector = np.random.randint(-10, 11, size=(1, ma_tran.shape[1]))
    return ma_tran + vector


def hang_ma_tran(ma_tran):
    return np.linalg.matrix_rank(ma_tran)


def phan_tich_svd(ma_tran):
    U, S, Vt = np.linalg.svd(ma_tran)
    return U, S, Vt


if __name__ == "__main__":
    N, M = map(int, input("Nhập số dòng và số cột của ma trận: ").split())
    ma_tran = tao_ma_tran(N, M)
    print("Ma trận gốc:\n", ma_tran)

    print("\n(1) Định thức ma trận:", dinh_thuc(ma_tran))
    print("\n(2) Ma trận nghịch đảo:\n", nghich_dao(ma_tran))
    print("\n(3) Ma trận sau khi sắp xếp theo hàng:\n", sap_xep_hang(ma_tran))
    print("\n(4) Ma trận sau khi sắp xếp theo cột:\n", sap_xep_cot(ma_tran))
    print("\n(5) Ma trận sau khi sắp xếp theo giá trị trung bình của từng hàng:\n",
          sap_xep_theo_trung_binh_hang(ma_tran))

    r, c, v = map(int, input("Nhập dòng, cột và giá trị mới để cập nhật: ").split())
    result = thay_doi_phan_tu(ma_tran, r, c, v)
    print("\n(6) Ma trận sau khi thay đổi phần tử:", result if isinstance(result, str) else "\n" + str(result))

    col = int(input("Nhập vị trí cột muốn tăng giá trị lên 2: "))
    print("\n(7) Ma trận sau khi thay đổi giá trị cột:\n", thay_doi_cot(ma_tran, col))

    print("\n(8) Ma trận sau khi cộng thêm vector:\n", cong_vector(ma_tran))
    print("\n(9) Hạng của ma trận:", hang_ma_tran(ma_tran))

    U, S, Vt = phan_tich_svd(ma_tran)
    print("\n(10) Phân tích SVD:\nU =", U, "\nS =", S, "\nVt =", Vt)
