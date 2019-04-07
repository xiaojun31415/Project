using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.OleDb;

namespace importExcel
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btn_click(object sender, EventArgs e)
        {

            string connString = "server=localhost;database=contact;user id=root;password=1234";
            System.Windows.Forms.OpenFileDialog fd = new OpenFileDialog();
            if (fd.ShowDialog() == DialogResult.OK)
            {
                TransferData(fd.FileName, "infor", connString);
            }
        }

        private void TransferData(string excelFile,string sheetName,string connectionString)
        {
            DataSet ds = new DataSet();

            try
            {
                string strConn = "Provider=Microsoft.Jet.OLEDB.4.0;" + "Data Source=" + excelFile + ";" + "Extended Properties=Excel 8.0;";
                OleDbConnection conn = new OleDbConnection(strConn);
                conn.Open();
                string strExcel = "";
                OleDbDataAdapter myCommand = null;
                strExcel = string.Format("select * from [{0}$]", sheetName);
                myCommand = new OleDbDataAdapter(strExcel, strConn);
                myCommand.Fill(ds, sheetName);
                string strSql = string.Format("if not exists( select * from sysobjects where name='{0} create table {0}'(",sheetName);
                foreach (System.Data.DataColumn c in ds.Tables[0].Columns) 
                {
                    strSql += string.Format("[{0}] varchar(255),", c.ColumnName);

                }
                strSql = strSql.Trim(',') + ")";
                using (System.Data.SqlClient.SqlConnection sqlconn=new System.Data.SqlClient.SqlConnection(connectionString))
                {
                    sqlconn.Open();
                    System.Data.SqlClient.SqlCommand command = sqlconn.CreateCommand();
                    command.CommandText = strSql;
                    command.ExecuteNonQuery();
                    sqlconn.Close();
                }
                using (System.Data.SqlClient.SqlBulkCopy bcp = new System.Data.SqlClient.SqlBulkCopy(connectionString))
                {
                    bcp.SqlRowsCopied += new System.Data.SqlClient.SqlRowsCopiedEventHandler(bcp_SqlRowsCopied);
                    bcp.BatchSize = 100;
                    bcp.NotifyAfter = 100;
                    bcp.DestinationTableName = sheetName;
                    bcp.WriteToServer(ds.Tables[0]);
                }

            }
            catch(Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.Message);
            }
        }

        void bcp_SqlRowCopied(object sender,System.Data.SqlClient.SqlRowsCopiedEventArgs e)
        {
            this.Text = e.RowsCopied.ToString();
            this.Update();
        }
    }
}
