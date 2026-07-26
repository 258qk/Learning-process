/**
 * ============================================================
 *  C语言水平检测 — 4阶段递进题目
 *  说明：每个阶段有独立题目，请按顺序完成。
 *        每道题标注了预计耗时和考察点。
 *        代码中标注了 // TODO: 的位置需要你来实现。
 * ============================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

/* ==================== 阶段一：基础语法与指针 ====================
 * 考察：数组、指针、字符串、基本算法
 * 难度：★☆☆☆☆   预计耗时：20分钟
 * -------------------------------------------------------- */

// 题目1-1：数组反转（5分）
// 要求：将数组原地反转，不允许使用额外数组
void reverse_array(int *arr, int len) {
    // TODO: 实现数组反转
    int l = len -1;
    int temp;
    {
        for (int i=0;i<len/2;i++) 
        {
            temp = arr[i];
            arr[i] = arr[l-i];
            arr[l-i] = temp;
        }
    }
}

// 题目1-2：字符串压缩（10分）
// 要求：统计连续字符出现次数，"aaabb" → "a3b2"
//       若压缩后不比原串短，则返回原串的副本
// 返回：压缩后的字符串（调用者负责 free）
char *compress_string(const char *src) {
    // TODO: 实现字符串压缩
    int len = strlen(src);
    char *compressed = malloc(2 * len + 1);
    int j = 0;
    int count = 1;
   for (int i = 0; src[i] != '\0'; i++) {
        if (src[i] == src[i + 1]) {
            count++;  // 相等就累加
        } else {
            compressed[j++] = src[i];      // 写入字母
            j += sprintf(compressed + j, "%d", count); // 写入次数
            count = 1; 
        }
    }
    compressed[j] = '\0';
    if(strlen(compressed)<strlen(src))
        return compressed;
    else
    {
        char *original = malloc(len + 1); 
        strcpy(original, src);
        free(compressed);
        return original;
    }
}

// 题目1-3：二级指针理解（5分）
// 要求：不修改函数体，写出输出结果（写在下方注释中）
void pointer_quiz() {
    int a = 10, b = 20;
    int *p = &a;
    int **pp = &p;
    *pp = &b;
    **pp = 30;
    printf("a=%d, b=%d, *p=%d\n", a, b, *p);
    // TODO: 你的答案 → a=____, b=____, *p=____
}

/* ==================== 阶段二：结构体与动态内存 ====================
 * 考察：struct、malloc/free、链表基础、函数封装
 * 难度：★★☆☆☆   预计耗时：25分钟
 * -------------------------------------------------------- */

// 题目2-1：动态数组（15分）
// 定义结构体 DynamicArray，支持以下操作：
//   - create(initial_capacity)  → 创建
//   - push_back(arr, value)     → 尾部追加（容量不足时自动扩容2倍）
//   - get(arr, index)           → 返回指定位置元素
//   - size(arr)                 → 返回当前元素个数
//   - destroy(arr)              → 销毁，释放所有内存

typedef struct {
    int *data;
    int  capacity;  // 当前容量
    int  length;    // 已有元素数
} DynamicArray;

DynamicArray *da_create(int initial_capacity) {
    // TODO
    DynamicArray *arr = malloc(sizeof(DynamicArray));
    arr->data = malloc(initial_capacity * sizeof(int));
    arr->capacity = initial_capacity;
    arr->length = 0;
    return arr;
}

void da_push_back(DynamicArray *arr, int value) {
    // TODO: 满了就 realloc 到 2 倍
    if(arr->capacity == arr->length)
    {
        arr->data = realloc(arr->data,2*arr->capacity*sizeof(int));
        arr->capacity *= 2;
    }
    arr->data[arr->length] = value;
    arr-> length++;
}

int da_get(DynamicArray *arr, int index) {
    // TODO: 越界返回 -1
    int i = 0;
    if(index >= arr->length || index < 0) 
        return -1;
    else
    {
        i = arr->data[index];
        return i;
    }
}

int da_size(DynamicArray *arr) {
    // TODO
    return arr->length;
}

void da_destroy(DynamicArray *arr) {
    // TODO
    free(arr->data);
    free(arr);
}

// 题目2-2：单向链表反转（10分）
// 要求：就地反转，只修改指针，不创建新节点

typedef struct Node {
    int           val;
    struct Node  *next;
} Node;

Node *reverse_list(Node *head) {
    // TODO
    return NULL;
}

// 辅助函数：创建链表节点
Node *new_node(int val) {
    Node *n = (Node *)malloc(sizeof(Node));
    n->val = val;
    n->next = NULL;
    return n;
}

/* ==================== 阶段三：位操作与函数指针 ====================
 * 考察：位运算、函数指针、回调机制（嵌入式核心技能）
 * 难度：★★★☆☆   预计耗时：25分钟
 * -------------------------------------------------------- */

// 题目3-1：寄存器位域操作（10分）
// 模拟 32 位寄存器，实现以下操作（不允许使用结构体位域语法）

// 设置 reg 的第 bit 位为 1
void reg_set_bit(uint32_t *reg, int bit) {
    // TODO
    *reg |= (1<<bit);
}

// 清除 reg 的第 bit 位
void reg_clear_bit(uint32_t *reg, int bit) {
    // TODO
    *reg &= ~(1<<bit);
}

// 将 reg 的 [high:low] 位设置为 value（保留其他位不变）
void reg_write_field(uint32_t *reg, int high, int low, uint32_t value) {
    // TODO
    int width;
    width = high - low+1;
    uint32_t mask = ((1<<width) -1)<<low;
    *reg &= ~mask;
    *reg |= (value << low) & mask;
}

// 读取 reg 的 [high:low] 位的值
uint32_t reg_read_field(uint32_t reg, int high, int low) {
    // TODO
    int width;
    width = high - low +1;
    uint32_t  mask = ((1<<width) -1);
    return (reg>>low) & mask;
}

// 题目3-2：回调排序引擎（15分）
// 要求：实现通用排序函数 sort，接受函数指针作为比较器
//       然后用它完成：按绝对值升序排序、按字符串长度升序排序

typedef int (*CompareFunc)(const void *, const void *);

void sort(void *arr, int n, int elem_size, CompareFunc cmp) {
    // TODO: 冒泡排序即可，需要按 elem_size 交换元素
}

// 比较器1：整数按绝对值升序
int cmp_abs(const void *a, const void *b) {
    // TODO
    return 0;
}

// 比较器2：字符串按长度升序
int cmp_strlen(const void *a, const void *b) {
    // TODO
    return 0;
}

/* ==================== 阶段四：综合实战 ====================
 * 考察：多知识点融合、设计能力
 * 难度：★★★★☆   预计耗时：30分钟
 * -------------------------------------------------------- */

/**
 * 题目4：简易传感器管理器（30分）
 *
 * 背景：模拟嵌入式系统中的多传感器管理
 * 要求实现一个 SensorManager，支持：
 *
 *   1. 注册传感器（名字字符串 + 设备地址4字节用uint32_t表示）
 *   2. 向传感器写入"配置值"（用位域方式写入地址的特定位段）
 *   3. 通过名字查找传感器并打印信息
 *   4. 遍历所有传感器，调用回调函数执行"采样"动作
 *   5. 销毁管理器释放所有内存
 *
 * 提示：用链表存储传感器，传感器结构体自己设计
 */

// TODO: 定义 Sensor 结构体
// TODO: 定义 SensorManager 结构体

// TODO: 实现 sm_create / sm_register / sm_config / sm_find / sm_foreach / sm_destroy

/* ==================== 主函数：测试入口 ==================== */

int main(void) {
    printf("===== C语言水平检测 =====\n");
    printf("请从阶段一开始逐题完成，完成后运行验证。\n\n");

    // ===== 阶段一测试 =====
    printf("--- 阶段一 ---\n");
    int arr1[] = {1, 2, 3, 4, 5};
    reverse_array(arr1, 5);
    printf("1-1 反转: %d %d %d %d %d (期望: 5 4 3 2 1)\n",
           arr1[0], arr1[1], arr1[2], arr1[3], arr1[4]);

    char *s = compress_string("aaabb");
    printf("1-2 压缩: %s (期望: a3b2)\n", s);
    free(s);

    s = compress_string("abc");
    printf("1-2 短串: %s (期望: abc)\n", s);
    free(s);

    printf("1-3 指针题 -- ");
    pointer_quiz();

    // ===== 阶段二测试 =====
    printf("\n--- 阶段二 ---\n");
    DynamicArray *da = da_create(2);
    da_push_back(da, 10);
    da_push_back(da, 20);
    da_push_back(da, 30);  // 触发扩容
    printf("2-1 size=%d, [0]=%d, [2]=%d (期望: size=3, [0]=10, [2]=30)\n",
           da_size(da), da_get(da, 0), da_get(da, 2));

    Node *head = new_node(1);
    head->next = new_node(2);
    head->next->next = new_node(3);
    head = reverse_list(head);
    printf("2-2 链表反转: ");
    for (Node *p = head; p; p = p->next) printf("%d ", p->val);
    printf("(期望: 3 2 1)\n");

    // 释放
    while (head) { Node *t = head; head = head->next; free(t); }
    da_destroy(da);

    // ===== 阶段三测试 =====
    printf("\n--- 阶段三 ---\n");
    uint32_t reg = 0x00FF0000;
    reg_clear_bit(&reg, 16);
    printf("3-1 clear_bit: 0x%08X (期望: 0x00FE0000)\n", reg);
    reg = 0;
    reg_write_field(&reg, 7, 0, 0xAB);
    printf("3-1 write_field: 0x%08X (期望: 0x000000AB)\n", reg);
    printf("3-1 read_field: 0x%02X (期望: 0xAB)\n", (unsigned)reg_read_field(reg, 7, 0));

    int arr3[] = {-5, 3, -1, 8, -2, 0};
    sort(arr3, 6, sizeof(int), cmp_abs);
    printf("3-2 按绝对值排序: ");
    for (int i = 0; i < 6; i++) printf("%d ", arr3[i]);
    printf("(期望: 0 -1 -2 3 -5 8)\n");

    // ===== 阶段四测试 =====
    printf("\n--- 阶段四 ---\n");
    printf("TODO: 完成 SensorManager 后取消下方注释运行\n");
    // SensorManager *sm = sm_create();
    // sm_register(sm, "TEMP",  0x0000FF00);
    // sm_register(sm, "PRESS", 0x0000AA00);
    // ... 更多测试

    printf("\n===== 测试结束 =====\n");
    return 0;
}
