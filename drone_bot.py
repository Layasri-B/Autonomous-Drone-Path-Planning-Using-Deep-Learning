"""
drone_bot.py
-------------
Main entry point for the Autonomous Drone Path Planning Telegram Bot.
"""

import numpy as np
import nest_asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from environment import Environment
from planner import DronePathPlanner
from utils import generate_video

nest_asyncio.apply()

TOKEN = "Telegram_bot_token"  # Replace this with your token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛸 Welcome to the Autonomous Drone Path Planner!\n\n"
        "Send your start and goal coordinates in this format:\n"
        "/start_goal x1,y1,z1 x2,y2,z2\n\n"
        "Example:\n/start_goal 0,0,0 20,20,15"
    )


async def get_coordinates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles /start_goal command.
    Reads coordinates, generates random environment, plans the path,
    computes metrics, and sends results + video.
    """
    try:
        message_text = update.message.text.strip().split()
        if len(message_text) != 3:
            raise ValueError("Expected format: /start_goal x1,y1,z1 x2,y2,z2")

        _, start_str, goal_str = message_text
        start = np.array([float(x) for x in start_str.split(',')])
        goal = np.array([float(x) for x in goal_str.split(',')])

        await update.message.reply_text(
            f"✅ Coordinates received!\nStart: {start}\nGoal: {goal}\n\n"
            "🎲 Generating random obstacles and planning path..."
        )

        # Generate environment and plan
        env = Environment(num_obstacles=5, space_limits=(0, 30))
        planner = DronePathPlanner(env)

        # Generate video and calculate metrics
        video_filename, total_distance, min_obstacle_dist, efficiency, accuracy = generate_video(
            planner, env, start, goal, filename="drone_path.mp4"
        )

        # Rename metrics for clarity
        precision_accuracy = accuracy
        path_efficiency = efficiency

        # Prepare clean output (no obstacle coordinates)
        result_text = (
            f"📊 Drone Path Results\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"Total Path Length: {total_distance:.2f} units\n"
            f"Path Efficiency: {path_efficiency:.2f}%\n"
            f"Precision Accuracy: {precision_accuracy:.2f}%\n"
            f"Minimum Distance to Obstacles: {min_obstacle_dist:.2f} units"
        )

        # Send metrics and video
        await update.message.reply_text(result_text)

        with open(video_filename, 'rb') as video_file:
            await update.message.reply_video(video=video_file)

    except Exception as e:
        await update.message.reply_text(
            "❌ Invalid input or an error occurred.\n\n"
            "Please use the format:\n/start_goal x1,y1,z1 x2,y2,z2\n\n"
            f"Error: {e}"
        )


def main():
    print("🤖 Starting the Autonomous Drone Path Planning Bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("start_goal", get_coordinates))
    app.run_polling()


if __name__ == "__main__":
    main()
