from flask import Flask
from config import Config

from auth.routes import auth_bp
from expenses.routes import expenses_bp
from incomes.routes import incomes_bp
from categories.routes import categories_bp
from dashboard.routes import dashboard_bp
from stats.routes import stats_bp
from messages.routes import messages_bp
from budgets.routes import budgets_bp
from users.routes import users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(expenses_bp, url_prefix="/expenses")
    app.register_blueprint(incomes_bp, url_prefix="/incomes")
    app.register_blueprint(categories_bp, url_prefix="/categories")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(stats_bp, url_prefix="/stats")
    app.register_blueprint(messages_bp, url_prefix="/messages")
    app.register_blueprint(budgets_bp, url_prefix="/budgets")
    app.register_blueprint(users_bp, url_prefix="/users")
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
