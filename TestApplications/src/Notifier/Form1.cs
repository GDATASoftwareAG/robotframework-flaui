using System;
using System.Windows.Forms;

namespace NotifierTest
{
    public sealed partial class Notifier : Form
    {
        public Notifier(string title = "Notifier", bool disableTimer = false)
        {
            InitializeComponent();

            Text = title;

            if (disableTimer) return;

            var aTimer = new Timer
            {
                Interval = 8000,
                Enabled = true,
            };

            aTimer.Tick += CloseWindow;
        }

        public void CloseWindow(object source, EventArgs e)
        {
            Close();
        }
    }
}
