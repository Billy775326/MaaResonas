import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体中文
plt.rcParams['axes.unicode_minus'] = False    # 解决负号 '-' 显示为方块的问题

# 示例数据...
epochs = np.arange(0, 51)
train_classification_loss = 0.6 * np.exp(-epochs / 10) + 0.2
validat_classification_loss = 0.5 * np.exp(-epochs / 10) + 0.2
train_localization_loss = -0.4 + 0.7 * (1 - np.exp(-epochs / 10))
validat_localization_loss = -0.3 + 0.8 * (1 - np.exp(-epochs / 10))
train_accuracy = 1 - 0.9 * np.exp(-epochs / 10)
validat_accuracy = 1 - 0.95 * np.exp(-epochs / 10)
train_map_0_5 = 1 - np.exp(-epochs / 5)
validat_map_0_5 = 1 - np.exp(-epochs / 6)

# 创建图形和子图...
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0, 0].plot(epochs, train_classification_loss, label='Train', color='blue')
axs[0, 0].plot(epochs, validat_classification_loss, label='Validation', color='orange')
axs[0, 0].set_title('训练与验证损失曲线')
axs[0, 0].set_xlabel('Epochs')
axs[0, 0].set_ylabel('Loss')
axs[0, 0].legend()

axs[0, 1].plot(epochs, train_localization_loss, label='Train', color='blue')
axs[0, 1].plot(epochs, validat_localization_loss, label='Validation', color='orange')
axs[0, 1].set_title('训练与验证损失对比')
axs[0, 1].set_xlabel('Epochs')
axs[0, 1].set_ylabel('Loss')
axs[0, 1].legend()

axs[1, 0].plot(epochs, train_accuracy, label='Train', color='blue')
axs[1, 0].plot(epochs, validat_accuracy, label='Validation', color='orange')
axs[1, 0].set_title('训练与验证准确率曲线')
axs[1, 0].set_xlabel('Epochs')
axs[1, 0].set_ylabel('Accuracy')
axs[1, 0].legend()

axs[1, 1].plot(epochs, train_map_0_5, label='Train', color='blue')
axs[1, 1].plot(epochs, validat_map_0_5, label='Validation', color='orange')
axs[1, 1].set_title('训练与验证mAP@0.5曲线')
axs[1, 1].set_xlabel('Epochs')
axs[1, 1].set_ylabel('mAP@0.5')
axs[1, 1].legend()

plt.tight_layout()
plt.show()