{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "mount_file_id": "1nkc9L3t6L9hcwB6uEh64BefhWm5tYqPM",
      "authorship_tag": "ABX9TyNUQgMuL1hgCUP0qyeE7Lc6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JIXG123/emergency-ryousan/blob/main/hello_world.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "\n",
        "def story(x):\n",
        "  print(str(x))\n",
        "  time.sleep(1)\n",
        "\n",
        "def opening():\n",
        "  story(\"これはテキストベーストRPGゲームです。\")\n",
        "  story(\"あなたがこれがゲームだと思うかどうかは自由です。\")\n",
        "  story(\"デッデデレー\")\n",
        "  start_q = input(\"スタートと入力して開始、設定と入力して設定を開きます。\")\n",
        "  while start_q != \"\":\n",
        "    if start_q == \"スタート\":\n",
        "      return start()\n",
        "    elif start_q == \"設定\":\n",
        "      return setting()\n",
        "    else:\n",
        "      story(\"ちょっと何言ってるかわかんないw大丈夫？僕はスタートか設定と入力してと言ったんだよ？\")\n",
        "      #無限ループ\n",
        "\n",
        "def start():\n",
        "  print(\"あらすじ\")\n",
        "  time.sleep(3)\n",
        "  story(\"昔々あるところにお爺さんとお婆さんがいました。\")\n",
        "  story(\"2人はある玉を持っていました。\")\n",
        "  story(\"ある日、2人は間違って玉を割ってしまいました。\")\n",
        "  story(\"玉のかけらは世界に散らばり、そのうち二つはお爺さんとお婆さんが持っています。\")\n",
        "  story(\"あなたはバカ\")\n",
        "  time.sleep(3)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "def setting():\n",
        "  print(\"setting? What's that?\")\n",
        "\n",
        "\n",
        "opening()"
      ],
      "metadata": {
        "id": "jNUwK31-Aqgj",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "75aefc3f-bc47-4589-ea95-f1c20c8cc891"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "これはテキストベーストRPGゲームです。\n",
            "あなたがこれがゲームだと思うかどうかは自由です。\n",
            "デッデデレー\n",
            "スタートと入力して開始、設定と入力して設定を開きます。スタート\n",
            "あらすじ\n",
            "昔々あるところにお爺さんとお婆さんがいました。\n",
            "2人はある玉を持っていました。\n",
            "ある日、2人は間違って玉を割ってしまいました。\n",
            "玉のかけらは世界に散らばり、そのうち二つはお爺さんとお婆さんが持っています。\n",
            "あなたはバカ\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip3 install pygame"
      ],
      "metadata": {
        "id": "yR2CBSsPXt8n",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "721a8a94-4ea4-4d7e-a620-d3929228c2c9"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pygame in /usr/local/lib/python3.11/dist-packages (2.6.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip3 install numpy"
      ],
      "metadata": {
        "id": "Hx7u4HS9jXPY",
        "outputId": "9f6c3652-0410-4a12-e95f-af95d0dbfe4e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: numpy in /usr/local/lib/python3.11/dist-packages (1.26.4)\n"
          ]
        }
      ]
    }
  ]
}