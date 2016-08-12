"""empty message

Revision ID: 9c57eb87e918
Revises: None
Create Date: 2016-08-11 22:23:51.191035

"""

# revision identifiers, used by Alembic.
revision = '9c57eb87e918'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('committee_meetings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('committee', sa.Enum('Evaluations', 'History', 'Social', 'Opcomm', 'R&D', 'House Improvements', 'Financial', 'Chairman', name='committees_enum'), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conditional',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.Column('date_due', sa.Date(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('status', sa.Enum('Pending', 'Passed', 'Failed', name='conditional_enum'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('current_coops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('freshman_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('eval_date', sa.Date(), nullable=False),
    sa.Column('onfloor_status', sa.Boolean(), nullable=True),
    sa.Column('room_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('freshman_eval_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('freshman_project', sa.Enum('Pending', 'Passed', 'Failed', name='freshman_project_enum'), nullable=False),
    sa.Column('eval_date', sa.DateTime(), nullable=False),
    sa.Column('signatures_missed', sa.Integer(), nullable=False),
    sa.Column('social_events', sa.Text(), nullable=True),
    sa.Column('other_notes', sa.Text(), nullable=True),
    sa.Column('freshman_eval_result', sa.Enum('Pending', 'Passed', 'Failed', name='freshman_eval_enum'), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('house_meetings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('housing_evals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('social_attended', sa.Text(), nullable=False),
    sa.Column('social_hosted', sa.Text(), nullable=False),
    sa.Column('technical_attended', sa.Text(), nullable=False),
    sa.Column('technical_hosted', sa.Text(), nullable=False),
    sa.Column('projects', sa.Text(), nullable=False),
    sa.Column('comments', sa.Text(), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('major_projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('status', sa.Enum('Pending', 'Passed', 'Failed', name='major_project_enum'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('onfloor_datetime',
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('onfloor_granted', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('uid', 'onfloor_granted')
    )
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('housing_form_active', sa.Boolean(), nullable=True),
    sa.Column('intro_form_active', sa.Boolean(), nullable=True),
    sa.Column('site_lockdown', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spring_evals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.Column('status', sa.Enum('Pending', 'Passed', 'Failed', name='spring_eval_enum'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('technical_seminars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('freshman_committee_attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fid', sa.Integer(), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fid'], ['freshman_accounts.id'], ),
    sa.ForeignKeyConstraint(['meeting_id'], ['committee_meetings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('freshman_hm_attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fid', sa.Integer(), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.Column('excuse', sa.Text(), nullable=True),
    sa.Column('attendance_status', sa.Enum('Attended', 'Excused', 'Absent', name='attendance_enum'), nullable=True),
    sa.ForeignKeyConstraint(['fid'], ['freshman_accounts.id'], ),
    sa.ForeignKeyConstraint(['meeting_id'], ['house_meetings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('freshman_seminar_attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fid', sa.Integer(), nullable=False),
    sa.Column('seminar_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fid'], ['freshman_accounts.id'], ),
    sa.ForeignKeyConstraint(['seminar_id'], ['technical_seminars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member_committee_attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meeting_id'], ['committee_meetings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member_hm_attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.Column('excuse', sa.Text(), nullable=True),
    sa.Column('attendance_status', sa.Enum('Attended', 'Excused', 'Absent', name='attendance_enum'), nullable=True),
    sa.ForeignKeyConstraint(['meeting_id'], ['house_meetings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member_seminar_attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.Column('seminar_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['seminar_id'], ['technical_seminars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member_seminar_attendance')
    op.drop_table('member_hm_attendance')
    op.drop_table('member_committee_attendance')
    op.drop_table('freshman_seminar_attendance')
    op.drop_table('freshman_hm_attendance')
    op.drop_table('freshman_committee_attendance')
    op.drop_table('technical_seminars')
    op.drop_table('spring_evals')
    op.drop_table('settings')
    op.drop_table('onfloor_datetime')
    op.drop_table('major_projects')
    op.drop_table('housing_evals')
    op.drop_table('house_meetings')
    op.drop_table('freshman_eval_data')
    op.drop_table('freshman_accounts')
    op.drop_table('current_coops')
    op.drop_table('conditional')
    op.drop_table('committee_meetings')
    ### end Alembic commands ###
